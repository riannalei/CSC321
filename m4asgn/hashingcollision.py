import hashlib
import random
import string
import time
from collections import defaultdict
import matplotlib.pyplot as plt

# Step 1a: function to generate SHA256 hash
def sha256_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Step 1b: function to calculate Hamming distance between two hashes
def hamming_distance(hash1, hash2):
    bin1 = bin(int(hash1, 16))[2:].zfill(256)
    bin2 = bin(int(hash2, 16))[2:].zfill(256)
    return sum(bit1 != bit2 for bit1, bit2 in zip(bin1, bin2))

# Step 1b: function to flip a specific bit in a string
def flip_bit(input_str, bit_position):
    byte_array = bytearray(input_str.encode())
    byte_index = bit_position // 8
    bit_index = bit_position % 8
    byte_array[byte_index] ^= 1 << bit_index
    return byte_array.decode('latin1')  # Use latin1 to handle non-printable characters

# Step 1a: hashing arbitrary inputs
print("--- Step 1a: Hashing Arbitrary Inputs ---")
input1 = "hello world"
hash1 = sha256_hash(input1)
print(f"Input: {input1} -> Hash: {hash1}")

input2 = "cryptography is fun"
hash2 = sha256_hash(input2)
print(f"Input: {input2} -> Hash: {hash2}")

# Step 1b: observing the Avalanche Effect (1-bit difference)
print("\n--- Step 1b: Avalanche Effect ---")
original = "hello world"
modified = flip_bit(original, 0)  # flip the first bit

hash_original = sha256_hash(original)
hash_modified = sha256_hash(modified)

print(f"Original: {original} -> {hash_original}")
print(f"Modified: {modified} -> {hash_modified}")
print(f"Hamming Distance: {hamming_distance(hash_original, hash_modified)} bits")

# Step 1c: finding Collisions in Truncated SHA256 Hashes
def find_collisions(bit_lengths):
    collision_data = defaultdict(list)

    for bits in bit_lengths:
        seen_hashes = {}
        start_time = time.time()
        attempts = 0

        while True:
            attempts += 1
            random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            full_hash = sha256_hash(random_string)
            truncated_hash = full_hash[:bits // 4]  # truncate the hash to the specified bits

            if truncated_hash in seen_hashes:
                elapsed_time = time.time() - start_time
                collision_data['digest_size'].append(bits)
                collision_data['time'].append(elapsed_time)
                collision_data['inputs'].append(attempts)
                print(f"Collision found for {bits} bits after {attempts} attempts in {elapsed_time:.2f} seconds.")
                break
            else:
                seen_hashes[truncated_hash] = random_string

    return collision_data

# Step 1c: Testing for bit lengths from 8 to 50 bits
print("\n--- Step 1c: Finding Collisions in Truncated Hashes ---")
bit_lengths = list(range(8, 52, 2))  # check for 8, 10, 12, ..., 50 bits
collision_results = find_collisions(bit_lengths)

# digest Size vs Collision Time
plt.figure()
plt.plot(collision_results['digest_size'], collision_results['time'], marker='o')
plt.xlabel('Digest Size (bits)')
plt.ylabel('Collision Time (seconds)')
plt.title('Digest Size vs Collision Time')
plt.grid()
plt.show()

# digest Size vs Number of Inputs
plt.figure()
plt.plot(collision_results['digest_size'], collision_results['inputs'], marker='o')
plt.xlabel('Digest Size (bits)')
plt.ylabel('Number of Inputs to Collision')
plt.title('Digest Size vs Number of Inputs to Collision')
plt.grid()
plt.show()
