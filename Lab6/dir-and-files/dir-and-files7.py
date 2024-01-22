import os


def copy_content(file, destination):
    copied = open(file, 'r')
    lines = copied.readlines()
    destination = open(destination, 'a')
    for line in lines:
        destination.write(line + "\n")

    print("Copied")


path = "/Users/uakks/Desktop/junk/B.txt"
dest = "/Users/uakks/Desktop/junk/A.txt"
copy_content(path, dest)
