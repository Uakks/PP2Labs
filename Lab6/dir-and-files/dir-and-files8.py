import os


def delete_path(path):
    if not os.path.exists(path):
        print("Path does not exist")
        return 0

    os.remove(path)
    print("Deleted")


path = "/Users/uakks/Desktop/junk/Z.txt"
delete_path(path)