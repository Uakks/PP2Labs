import os


def create_files(path, n):
    os.chdir(path)
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in letters:
        if letter == n:
            f = open(f"{letter}.txt", "x", encoding="utf-8")
            break
        f = open(f"{letter}.txt", "x", encoding="utf-8")

    print("Files created")


num = input("Enter last letter to be created: ")
path1 = "/Users/uakks/Desktop/ICPC/Number Theory"
create_files(path1, num)
