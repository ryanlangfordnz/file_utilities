import sys
import os
import argparse
from datetime import datetime
import re


# set up parser for input
parser = argparse.ArgumentParser()

parser.add_argument("-p", "--path", help="Path")
parser.add_argument(
    "-f",
    "--format",
    help="Set the format of the timestamp using strftime conventions",
    required=False,
)
group = parser.add_mutually_exclusive_group()
group.add_argument(
    "-c", "--created", action="store_true", help="Rename the file with creation time"
)
group.add_argument(
    "-m",
    "--modified",
    action="store_true",
    help="Rename the file with modification time",
)


args = parser.parse_args()

# test that given format is valid
now = datetime.now()
try:
    datetime.strftime(now, args.format)
except ValueError:
    print("Invalid timestamp format")
    exit(1)

# check path is given
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
files = list(filter(lambda x: os.path.isfile(file_path + "\\" + x), objects))

# show the user a file so they can see effect in case they have  it wrong
print("The files will be timestamped like this:")
if args.created:
    file_time = os.path.getctime(file_path + "\\" + files[0])
else:
    file_time = os.path.getmtime(file_path + "\\" + file[0])
# convert timestamp float to datetime object
file_time = datetime.fromtimestamp(file_time)
# get extension
extension = re.findall(r"\.\w{3}", files[0])[-1]
print(file_path + "\\" + files[0][0:-4] + file_time.strftime(args.format) + extension)
# give the user an option to exit
exit_option = input("Is this the correct format Y/N:\n")
if exit_option in ["N", "n"]:
    exit(0)

for file in files:
    # check created or modified flags
    if args.created:
        file_time = os.path.getctime(file_path + "\\" + file)
    else:
        file_time = os.path.getmtime(file_path + "\\" + file)
    # convert timestamp float to datetime object
    file_time = datetime.fromtimestamp(file_time)
    # get extension
    extension = re.findall(r"\.\w{3}", file)[-1]
    # rename the file
    os.rename(
        file_path + "\\" + file,
        file_path + "\\" + file[0:-4] + file_time.strftime(args.format) + extension,
    )


# TODO deduplicate the format checking and renaming, make everything fstrings
