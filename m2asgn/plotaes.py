import matplotlib.pyplot as plt

block_sizes = [16, 64, 256, 1024, 8192, 16384]
aes_128 = [852162.93, 1107405.36, 1188924.50, 1204423.92, 1216070.25, 1217086.58]
aes_192 = [785701.67, 984845.42, 979788.02, 995690.71, 1000804.61, 999920.48]
aes_256 = [503066.13, 805425.10, 846423.57, 858605.41, 866683.16, 863199.59]

plt.figure(figsize=(8, 6))
plt.plot(block_sizes, aes_128, label='AES-128', marker='o')
plt.plot(block_sizes, aes_192, label='AES-192', marker='o')
plt.plot(block_sizes, aes_256, label='AES-256', marker='o')
plt.title('AES Performance: Block Size vs. Throughput')
plt.xlabel('block size (bytes)')
plt.ylabel('throughput (kB/s)')
plt.legend()
plt.grid(True)
plt.show()
