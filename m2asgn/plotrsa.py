import matplotlib.pyplot as plt

key_sizes = [512, 1024, 2048, 3072, 4096, 7680, 15360]
rsa_sign = [40791.0, 8431.5, 1372.3, 471.0, 215.6, 26.3, 5.0]
rsa_verify = [426802.0, 173817.4, 54574.8, 25726.5, 14875.3, 4370.9, 1115.6]
rsa_encrypt = [374978.2, 161385.1, 52595.8, 25141.3, 14628.7, 4337.0, 1108.9]
rsa_decrypt = [32808.9, 7966.3, 1349.0, 470.5, 215.0, 26.3, 4.9]

plt.figure(figsize=(8, 6))
plt.plot(key_sizes, rsa_sign, label='RSA Sign', marker='o')
plt.plot(key_sizes, rsa_verify, label='RSA Verify', marker='o')
plt.plot(key_sizes, rsa_encrypt, label='RSA Encrypt', marker='o')
plt.plot(key_sizes, rsa_decrypt, label='RSA Decrypt', marker='o')
plt.title('RSA Performance: Key Size vs. Throughput')
plt.xlabel('key Size (bits)')
plt.ylabel('throughput (ops/s)')
plt.legend()
plt.grid(True)
plt.show()
