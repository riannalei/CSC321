from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

#generating the AES key and IV 
key = get_random_bytes(16)  #AES 128 requires 16byte key 
iv = get_random_bytes(16)  #or CBC mode

def pad_pkcs7(data, block_size=16):
    """Add PKCS#7 padding to data."""
    padding_length = block_size - (len(data) % block_size)
    return data + bytes([padding_length] * padding_length)

def aes_ecb_encrypt(plaintext, key):
    """Encrypt plaintext using AES in ECB mode (manual implementation)."""
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = b""
    for i in range(0, len(plaintext), 16):
        block = plaintext[i:i+16]
        ciphertext += cipher.encrypt(block)
    return ciphertext

def aes_cbc_encrypt(plaintext, key, iv):
    """Encrypt plaintext using AES in CBC mode (manual implementation)."""
    cipher = AES.new(key, AES.MODE_ECB)  # Use ECB for individual block encryption
    ciphertext = b""
    previous_block = iv
    for i in range(0, len(plaintext), 16):
        block = plaintext[i:i+16]
        block = bytes([b ^ p for b, p in zip(block, previous_block)])
        encrypted_block = cipher.encrypt(block)
        ciphertext += encrypted_block
        previous_block = encrypted_block
    return ciphertext

def read_bmp_file(file_path):
    """Read BMP file, separating the header and body."""
    with open(file_path, "rb") as f:
        data = f.read()
    header = data[:54] 

    body = data[54:]
    return header, body

def write_bmp_file(file_path, header, encrypted_body):
    """Write encrypted BMP file, preserving the header."""
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
