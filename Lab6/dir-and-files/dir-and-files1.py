import os


def list_directories_and_files(path):
    try:
        entries = os.listdir(path)

        directories = [entry for entry in entries if os.path.isdir(os.path.join(path, entry))]
        files = [entry for entry in entries if os.path.isfile(os.path.join(path, entry))]

        print("Directories:")
        print(directories)

        print("\nFiles:")
        print(files)

        print("\nAll Directories and Files:")
        print(entries)

    except FileNotFoundError:
        print(f"The specified path '{path}' does not exist.")


# On my computer I have this path and it works
specified_path = "/Users/uakks/Desktop"
list_directories_and_files(specified_path)
