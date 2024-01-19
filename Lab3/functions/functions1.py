import math
import random
from itertools import permutations


# 1
def grams_to_ounces(grams):
    return grams / 28.3495231


# 2
def fahrenheit_to_celcium(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


# 3
def solve(numheads, numlegs):
    if numlegs % 2 == 1:
        print("Unreal")
        return 0
    initial = numheads
    while numlegs / 2 != numheads:
        numlegs -= 4
        numheads -= 1
    print(f"Number of rabbits: {initial - numheads}, chickens: {numheads}")


# solve(26, 96)

# 4
def primes(lst):
    i = 0
    while i < len(lst):
        deleted = False
        for j in range(2, lst[i]):
            if lst[i] % j == 0:
                lst.remove(lst[i])
                deleted = True
                break
        if not deleted:
            i += 1
    print(lst)


# primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])

# 5
def str_permuts(string):
    lst = permutations(string)
    for i in lst:
        print(i)


# str_permuts("abc")

# 6
def str_reversed(string):
    lst = string.split(" ")
    lst = reversed(lst)
    for i in lst:
        print(i, end=" ")


# str_reversed("Hello World")

# 7
def has_33(lst):
    for i in range(len(lst) - 1):
        if lst[i] == 3:
            if lst[i + 1] == 3:
                print(True)
                return True
    print(False)
    return False


# has_33([1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 3])
# 8
def spy_game(lst):
    cnt = 0
    for i in range(len(lst)):
        if cnt == 1 or cnt == 0:
            if lst[i] == 0:
                cnt += 1
        elif cnt == 2:
            if lst[i] == 7:
                print(True)
                return True
    print(False)
    return False


# spy_game([1,2,4,0,0,7,5])
# spy_game([1,0,2,4,0,5,7])
# spy_game([1,7,2,0,4,5,0])

# 9
def volume_sphere(radius):
    print((radius ** 3) * 4 * math.pi / 3)
    return (radius ** 3) * 4 * math.pi / 3


# volume_sphere(10)
# 10
def unique(lst):
    sorted_lst = sorted(lst)
    final = [sorted_lst[0]]
    for i in range(1, len(lst)):
        if sorted_lst[i] != sorted_lst[i-1]:
            final.append(sorted_lst[i])
    print(final)


# unique([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
# 11
def is_palindrome(string):
    print(string == string[::-1])
    return string == string[::-1]


# is_palindrome("abcba")
# is_palindrome("abcds")
# 12
def histogram(lst):
    for i in range(len(lst)):
        for j in range(lst[i]):
            print("*", end="")
        print("")


# histogram([4, 8, 6])
# 13
def Guess_Number(start, end):
    guess = random.randint(start, end)
    while True:
        tries = 1
        name = input("Hello! What is your name?")
        print("Well, " + name + ", I am thinking of a number between 1 and 20.")
        attempt = int(input("Take a guess."))
        while attempt != guess:
            tries += 1
            if attempt < guess:
                print("Your guess is too low")
                attempt = int(input("Take a guess."))
            else:
                print("Your guess is too high")
                attempt = int(input("Take a guess."))
        print(f"Good job, {name}! You guessed my number in {tries} guesses!")
        break


# Guess_Number(1, 20)
