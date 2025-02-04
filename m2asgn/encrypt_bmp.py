from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

#generating the random 16byte AES key and IV 
key = get_random_bytes(16)  
iv = get_random_bytes(16)  

#add padding so the data is multiple of 16 bytes 
def pad_pkcs7(data, block_size=16):
    padding_length = block_size - (len(data) % block_size)
    return data + bytes([padding_length] * padding_length)

#encrypt data in ECB mode block by block
def aes_ecb_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)  # create an AES cipher in ECB mode
    ciphertext = b""
    # process plaintext in chunks of 16 bytes
    for i in range(0, len(plaintext), 16):
        block = plaintext[i:i+16]
        ciphertext += cipher.encrypt(block)  # encrypt each block
    return ciphertext

#encrypt data in CBC mode block by block
def aes_cbc_encrypt(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_ECB) 
    ciphertext = b""
    previous_block = iv  # start chaining with the IV
    # process plaintext in chunks of 16 bytes
    for i in range(0, len(plaintext), 16):
        block = plaintext[i:i+16]
        # XOR the block with the previous ciphertext block (or IV)
        block = bytes([b ^ p for b, p in zip(block, previous_block)])
        encrypted_block = cipher.encrypt(block)  # encrypt the XORed block
        ciphertext += encrypted_block
        previous_block = encrypted_block  # update the chaining block
    return ciphertext

# read the BMP file and separate the header and pixel data
def read_bmp_file(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    header = data[:54] #BMP header is the first 54 bytes, and the rest is pixel data
    body = data[54:]
    return header, body

#write the header and encrypted pixel dtaa back to a new BMP file 
def write_bmp_file(file_path, header, encrypted_body):
    with open(file_path, "wb") as f:
        f.write(header + encrypted_body)

def main():
    file_path = "cp-logo.bmp"
    header, body = read_bmp_file(file_path)

    # add PKCS#7 padding to the body
    padded_body = pad_pkcs7(body)

    # encrypt using ECB and CBC
    ecb_ciphertext = aes_ecb_encrypt(padded_body, key)
    cbc_ciphertext = aes_cbc_encrypt(padded_body, key, iv)

    # write the encrypted BMP files
    write_bmp_file("encrypted_ecb.bmp", header, ecb_ciphertext)
    write_bmp_file("encrypted_cbc.bmp", header, cbc_ciphertext)

    print("encryption completed.")

if __name__ == "__main__":
    main()

#python3 encrypt_bmp.py
