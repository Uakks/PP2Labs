import os


def spec_path(path):
    if os.access(path, os.F_OK):
        print("The path exists")
    else:
        print("The path does not exist")

    if os.access(path, os.R_OK):
        print("The path is readable")
    else:
        print("The path is not readable")

    if os.access(path, os.W_OK):
        print("The path is writable")
    else:
        print("The path is not writable")

    if os.access(path, os.X_OK):
        print("The path is executable")
    else:
        print("The path is not executable")


# On my computer I have this path and it works
specified_path = "/Users/uakks/Desktop"
spec_path(specified_path)
