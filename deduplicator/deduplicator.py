import sys
import os
import hashlib
from collections import Counter
import argparse


# set up parser for input
parser = argparse.ArgumentParser()

parser.add_argument("-p", "--path", help="Path")

args = parser.parse_args()

if not args.path:
    print("Please enter a path using the -p flag")
    exit(1)

file_path = args.path

# check that the path is valid and not a file
if os.path.exists(file_path) == False or os.path.isdir(file_path) == False:
    print("Not a valid directory path sorry")
    exit(1)

# get a list of everything at the path
objects = os.listdir(file_path)
# pare it down to just the files
files = list(filter(lambda x: os.path.isfile(x), objects))

# Hashing the files to make sure they are unique or duplicated
BLOCK_SIZE = 65536  # The size of each read from the file


def hasher(filename):
    filename = file_path + "\\" + filename
    file_hash = (
        hashlib.sha256()
    )  # Create the hash object, can use something other than `.sha256()` if you wish
    with open(filename, "rb") as f:  # Open the file to read it's bytes
        fb = f.read(BLOCK_SIZE)  # Read from the file. Take in the amount declared above
        while len(fb) > 0:  # While there is still data being read from the file
            file_hash.update(fb)  # Update the hash
            fb = f.read(BLOCK_SIZE)  # Read the next block from the file
    return file_hash.hexdigest()


file_hashes = {x: hasher(x) for x in files}
hash_counter = Counter(file_hashes.values())

# early out if folder is duplicate free
if max(hash_counter.values()) == 1:
    print("Folder is duplicate free")
    exit(1)


# loop through and get rid of extra files
for file, hash in file_hashes.items():
    if hash_counter[hash] > 1:
        hash_counter[hash] -= 1
        os.remove(file_path + "\\" + file)

print("Folder is now duplicate free")
