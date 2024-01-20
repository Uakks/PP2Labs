import re

string = input("Enter a word: ")
# 1
print(re.findall("ab*", string))

# 2
print(re.findall("ab?b{2}", string))

# 3
print(re.findall("[a-z]*_+", string))

# 4
print(re.findall("[A-Z]{1}[a-z]*", string))

# 5
print(re.findall("a.*b", string))

# 6
print(re.sub("[ ,.]", ":", string))

# 7
print(re.sub("_", " ", string).title().replace(" ", ""))

# 8
print(re.split("[A-Z]", string))

# 9
lst = re.findall("[A-Z][^A-Z]*", string)
txt = ""
for word in lst:
    txt += (word + " ")

print(txt)

# 10
string = string[0].upper() + string[1:]
lst = re.findall("[A-Z][^A-Z]*", string)
txt = ""
for i in range(len(lst)):
    if i != len(lst) - 1:
        txt += lst[i].lower() + "_"
    else:
        txt += lst[i].lower()


print(txt)
