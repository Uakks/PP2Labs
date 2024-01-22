import os


def spec_path(path):
    if os.access(path, os.F_OK):
        print("The path exists")
        print(os.path.abspath(path))
    else:
        print("The path does not exist")


specified_path = "/Users/uakks/Desktop"
spec_path(specified_path)
