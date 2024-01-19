class Strings:
    def __init__(self):
        self.string = ""

    def print_string(self):
        return self.string.upper()

    def get_string(self):
        self.string = input("Enter a word: ")
        return self.string


t1 = Strings()
print(t1.get_string())
print(t1.print_string())