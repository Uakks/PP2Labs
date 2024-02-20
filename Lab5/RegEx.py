import re

file = open("Lab5 row (1).txt")
list_file = file.readlines()


# string = input("Enter a word: ")
# 1
def ab():
    for word in list_file:
        if len(re.findall("ab*", word)) != 0:
            print(word, " -> ", end="")
            print(re.findall("ab*", word))


# 2
def abbb():
    for word in list_file:
        if len(re.findall("ab?b{2}", word)) != 0:
            print(word, " -> ", end="")
            print(re.findall("ab?b{2}", word))


# 3
def lower_():
    for word in list_file:
        if len(re.findall("[a-z]*_+", word)) != 0:
            print(word, " -> ", end="")
            print(re.findall("[a-z]*_+", word))


# 4
def upper_lower():
    for word in list_file:
        if len(re.findall("[A-Z]{1}[a-z]*", word)) != 0:
            print(word, " -> ", end="")
            print(re.findall("[A-Z]{1}[a-z]*", word))


# 5
def from_a_to_b():
    for word in list_file:
        if len(re.findall("a.*b", word)) != 0:
            print(word, " -> ", end="")
            print(re.findall("a.*b", word))


# 6
def replace():
    for word in list_file:
        if len(re.findall("[ ,.]", word)) != 0:
            print(word, " -> ", end="")
            print(re.sub("[ ,.]", ":", word))


# 7
def snake_to_camel_case():
    for word in list_file:
        if len(re.findall("_", word)) != 0:
            print(word, " -> ", end="")
            print(re.sub("_", " ", word).title().replace(" ", ""))


# 8
def split_at_upper():
    for word in list_file:
        if len(re.findall("[A-Z]", word)) != 0:
            print(word, " -> ", end="")
            print(re.split("[A-Z]", word))


# 9
def insert_spaces():
    for word in list_file:
        if len(re.findall("ab*", word)) != 0:
            print(word, " -> ", end="")
            lst = re.findall("[A-Z][^A-Z]*", word)
            txt = ""
            for word1 in lst:
                txt += (word1 + " ")

            print(txt)


# 10
def camel_to_snake_case():
    for word in list_file:
        if len(re.findall("ab*", word)) != 0:
            print(word, " -> ", end="")
            lst = re.findall("[A-Z][^A-Z]*", word)
            txt = ""
            for i in range(len(lst)):
                if i != len(lst) - 1:
                    txt += lst[i].lower() + "_"
                else:
                    txt += lst[i].lower()

            print(txt)


# ab()
# abbb()
# lower_()
# upper_lower()
# from_a_to_b()
# replace()
# snake_to_camel_case()
# split_at_upper()
# insert_spaces()
# camel_to_snake_case()
