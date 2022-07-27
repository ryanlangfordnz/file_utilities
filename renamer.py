import sys
import os
import hashlib
from collections import Counter
import argparse
import re

# set up parser for input
parser = argparse.ArgumentParser()

parser.add_argument("-p", "--path", help="Path")
parser.add_argument(
    "-a", "--all", help="Renames all the files in the folder", required=False
)
parser.add_argument(
    "-s", "--single", help="Renames all copies of specified file", required=False
)

args = parser.parse_args()


if not args.path:
    print("Please enter a path using the -p flag")
    exit(1)

if not args.single and not args.all:
    print("Please use either the -a or -s flag")
    exit(1)

file_path = args.path

# check that the path is valid and not a file
if os.path.exists(file_path) == False or os.path.isdir(file_path) == False:
    print("Not a valid directory path sorry")
    exit(1)

# get a list of everything at the path
objects = os.listdir(file_path)


# pare it down to just the files
files = list(filter(lambda x: os.path.isfile(file_path + "\\" + x), objects))


# if -s flag is used, check that that file exists
if args.single and args.single not in files:
    print(f"File {args.single} does not exist at the specified path")

# if the -a flag is used, rename all files to the specified name + _XX
if args.all:
    for count, value in enumerate(files):
        extension = re.findall(r"\.\w{3}", value)[-1]

        os.rename(
            file_path + "\\" + value,
            file_path + "\\" + args.all + f"_0{count + 1 }{extension}",
        )
    print(f"Renamed {len(files)} files")
    exit(1)

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


# if -s flag is used and the file exists rename all copies of that file
if args.single and args.single in files:
    file_hashes = {x: hasher(x) for x in files}
    hash_counter = Counter(file_hashes.values())
    print(f"There are {hash_counter[file_hashes[args.single]]} copies of that file")
    rename = input(
        "Enter what you want to rename the files to. Copies will be in the format X_01,X_02 etc\nNew name:"
    )
    if rename == "":  # check for empty input
        print("That is not a valid file name, please try again")
        exit(1)
    for count, file in enumerate(files):
        if file_hashes[file] == file_hashes[args.single]:
            extension = re.findall(r"\.\w{3}", file)[-1]
            os.rename(
                file_path + "\\" + file,
                file_path + "\\" + rename + f"_0{count + 1 }{extension}",
            )
    print(f"Renamed {hash_counter[file_hashes[args.single]]} files")
    exit(1)
