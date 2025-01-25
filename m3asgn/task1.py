from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import random

def diffie_hellman():
    # Parameters
    q = int("B10B8F96A080E01DDE92DE5EAE5D54EC52C99FBCFB06A3C69A6A9DCA52D23B61"
            "6073E28675A23D189838EF1E2EE652C013ECB4AEA906112324975C3CD49B83BF"
            "ACCBDD7D90C4BD7098488E9C219A73724EFFD6FAE5644738FAA31A4FF55BCCC0"
            "A151AF5F0DC8B4BD45BF37DF365C1A65E68CFDA76D4DA708DF1FB2BC2E4A4371", 16)
    alpha = int("A4D1CBD5C3FD34126765A442EFB99905F8104DD258AC507FD6406CFF14266D31"
                "266FEA1E5C41564B777E690F5504F213160217B4B01B886A5E91547F9E2749F4"
                "D7FBD7D3B9A92EE1909D0D2263F80A76A6A24C087A091F531DBF0A0169B6A28A"
                "D662A4D18E73AFA32D779D5918D08BC8858F4DCEF97C2A24855E6EEB22B3B2E5", 16)

    # Alice's private key and public key
    X_A = random.randint(1, q - 1)  # Private key
    Y_A = pow(alpha, X_A, q)  # Public key

    # Bob's private key and public key
    X_B = random.randint(1, q - 1)  # Private key
    Y_B = pow(alpha, X_B, q)  # Public key

    # Exchange public keys and compute the shared secret
    s_A = pow(Y_B, X_A, q)  # Alice computes shared secret
    s_B = pow(Y_A, X_B, q)  # Bob computes shared secret

    # Ensure both shared secrets are the same
    assert s_A == s_B, "Shared secrets do not match!"
    shared_secret = s_A
    print(f"Shared Secret: {shared_secret}")

    # Derive a symmetric key from the shared secret
    symmetric_key = SHA256.new(str(shared_secret).encode()).digest()[:16]
    print(f"Symmetric Key: {symmetric_key.hex()}")

    # AES-CBC Encryption
    iv = b"1234567890123456"  # Initialization vector
    cipher = AES.new(symmetric_key, AES.MODE_CBC, iv)

    # Alice sends an encrypted message to Bob
    m0 = "Hi Bob!"
    c0 = cipher.encrypt(pad(m0.encode(), 16))
    print(f"Alice sends: {c0}")

    # Bob decrypts the message
    decipher = AES.new(symmetric_key, AES.MODE_CBC, iv)
    m0_decrypted = unpad(decipher.decrypt(c0), 16)
    print(f"Bob decrypts: {m0_decrypted.decode()}")

    # Bob sends an encrypted message to Alice
    m1 = "Hi Alice!"
    c1 = cipher.encrypt(pad(m1.encode(), 16))
    print(f"Bob sends: {c1}")

    # Alice decrypts the message
    m1_decrypted = unpad(decipher.decrypt(c1), 16)
    print(f"Alice decrypts: {m1_decrypted.decode()}")

diffie_hellman()
