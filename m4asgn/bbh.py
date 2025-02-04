import bcrypt
import time
from nltk.corpus import words
import nltk
nltk.download('words')

# load the NLTK word corpus and filter for words between 6 and 10 letters
word_list = [word.lower() for word in words.words() if 6 <= len(word) <= 10]

shadow_data = {
    "Bilbo": "$2b$08$J9FW66ZdPI2nrIMcOxFYI.qx268uZn.ajhymLP/YHaAsfBGP3Fnmq",
    "Gandalf": "$2b$08$J9FW66ZdPI2nrIMcOxFYI.q2PW6mqALUl2/uFvV9OFNPmHGNPa6YC",
    "Thorin": "$2b$08$J9FW66ZdPI2nrIMcOxFYI.6B7jUcPdnqJz4tIUwKBu8lNMs5NdT9q",
    "Fili": "$2b$09$M9xNRFBDn0pUkPKIVCSBzuwNDDNTMWlvn7lezPr8IwVUsJbys3YZm",
    "Kili": "$2b$09$M9xNRFBDn0pUkPKIVCSBzuPD2bsU1q8yZPlgSdQXIBILSMCbdE4Im",
    "Balin": "$2b$10$xGKjb94iwmlth954hEaw3O3YmtDO/mEFLIO0a0xLK1vL79LA73Gom",
    "Dwalin": "$2b$10$xGKjb94iwmlth954hEaw3OFxNMF64erUqDNj6TMMKVDcsETsKK5be",
    "Oin": "$2b$10$xGKjb94iwmlth954hEaw3OcXR2H2PRHCgo98mjS11UIrVZLKxyABK",
    "Gloin": "$2b$11$/8UByex2ktrWATZOBLZ0DuAXTQl4mWX1hfSjliCvFfGH7w1tX5/3q",
    "Dori": "$2b$11$/8UByex2ktrWATZOBLZ0Dub5AmZeqtn7kv/3NCWBrDaRCFahGYyiq",
    "Nori": "$2b$11$/8UByex2ktrWATZOBLZ0DuER3Ee1GdP6f30TVIXoEhvhQDwghaU12",
    "Ori": "$2b$12$rMeWZtAVcGHLEiDNeKCz8OiERmh0dh8AiNcf7ON3O3P0GWTABKh0O",
    "Bifur": "$2b$12$rMeWZtAVcGHLEiDNeKCz8OMoFL0k33O8Lcq33f6AznAZ/cL1LAOyK",
    "Bofur": "$2b$12$rMeWZtAVcGHLEiDNeKCz8Ose2KNe821.l2h5eLffzWoP01DlQb72O",
    "Durin": "$2b$13$6ypcazOOkUT/a7EwMuIjH.qbdqmHPDAC9B5c37RT9gEw18BX6FOay"
}

# brute-force a single user's password
def crack_password(username, full_hash):
    print(f"Cracking password for {username}...")
    start_time = time.time()

    for word in word_list:
        if bcrypt.checkpw(word.encode(), full_hash.encode()):
            elapsed_time = time.time() - start_time
            print(f"Password for {username} is '{word}' (found in {elapsed_time:.2f} seconds)")
            return (username, word, elapsed_time)

    print(f"Password for {username} not found.")
    return (username, None, None)

# Run the brute-force cracking for all users
results = []
for user, hash_value in shadow_data.items():
    result = crack_password(user, hash_value)
    results.append(result)

print("\n--- Summary of Cracked Passwords ---")
for username, password, time_taken in results:
    if password:
        print(f"{username}: {password} (Time: {time_taken:.2f} seconds)")
    else:
        print(f"{username}: Password not found.")
