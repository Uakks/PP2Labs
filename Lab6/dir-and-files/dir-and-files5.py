import os


def write_to_file(filename, lst):
    with open(filename, 'a') as f:
        for item in lst:
            f.write(item + "\n")
            print(f"{item} was written to file")


# 5 it works
list1 = ["Hello", "World"]
write_to_file('/Users/uakks/Desktop/junk/B.txt', list1)
