# 1
import math
import time

lst = [1, 2, 3, 4, 5]


def multiply(lst):
    product = 1
    for i in lst:
        product = product * i

    return product


print(multiply(lst))

# 2
word = input("Word: ")


def uppers_and_lowers(word):
    uppers = 0
    lowers = 0
    for letter in word:
        if letter.isupper():
            uppers += 1
        elif letter.islower():
            lowers += 1

    return uppers, lowers


print(uppers_and_lowers(word))

# 3
word1 = input("Word: ")
print(word1 == word1[::-1])

# 4
num = int(input("Sample input: "))
ms = int(input("ms: "))
time.sleep(ms / 1000)
print(f"Square root of {num} after {ms} milliseconds is {math.sqrt(num)}")

# 5
tup = (True, True, True, True)
print(all(tup))
