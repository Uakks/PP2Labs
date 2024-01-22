import os


def open_path(path):
    file = open(path)
    file_contents = len(file.readlines())
    return file_contents


# Using file from 5th Lab
path = "/Users/uakks/Downloads/Lab5 row.txt"
print(open_path(path))
