import bcrypt
import time

# Test word list to quickly check if the script works
test_words = ['password', 'bilbo', 'hobbit', 'ringbearer', 'middleearth']

# Bilbo's hash for testing
bilbo_hash = "$2b$08$J9FW66ZdPI2nrIMcOxFYI.qx268uZn.ajhymLP/YHaAsfBGP3Fnmq"

# Function to test cracking
def test_crack_password(username, full_hash, word_list):
    print(f"Testing password cracking for {username}...")
    start_time = time.time()

    for word in word_list:
        print(f"Trying: {word}")
        if bcrypt.checkpw(word.encode(), full_hash.encode()):
            elapsed_time = time.time() - start_time
            print(f"Password for {username} is '{word}' (found in {elapsed_time:.2f} seconds)")
            return (username, word, elapsed_time)

    print(f"Password for {username} not found in test list.")
    return (username, None, None)

# Run the test cracking process
result = test_crack_password("Bilbo", bilbo_hash, test_words)

# Print summary
username, password, time_taken = result
print("\n--- Test Result ---")
if password:
    print(f"{username}: {password} (Time: {time_taken:.2f} seconds)")
else:
    print(f"{username}: Password not found in test list.")
