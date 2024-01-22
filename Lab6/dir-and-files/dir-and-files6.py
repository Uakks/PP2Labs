import os


def create_files(path):
    os.chdir(path)
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        f = open(f"{letter}.txt", "x", encoding="utf-8")

    print("Files created")


path = "/Users/uakks/Desktop/junk"
create_files(path)
