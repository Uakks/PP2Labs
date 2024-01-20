# 1
def generates(n):
    for i in range(n+1):
        yield i**2


# for num in generates(int(input("Enter n: "))):
#     print(num)

# 2
def evens(n):
    for i in range(n):
        if i % 2 == 0:
            yield i


# lst = list(evens(int(input("Enter n: "))))
# for num in range(len(lst)):
#     if num == len(lst)-1:
#         print(lst[num], end="")
#     else:
#         print(lst[num], end=", ")

# 3
def divisible(n):
    for i in range(1,n+1):
        if i % 12 == 0:
            yield i


# lst = list(divisible(int(input("Enter n: "))))
# for num in range(len(lst)):
#     if num == len(lst)-1:
#         print(lst[num], end="")
#     else:
#         print(lst[num], end=", ")

# 4
def squares(a, b):
    for i in range(a, b+1):
        yield i**2


# for num in squares(int(input("Enter a: ")), int(input("Enter b: "))):
#     print(num)

# 5
def from_n_to_0(n):
    for i in range(n, -1, -1):
        yield i


# for i in from_n_to_0(12):
#     print(i, end=' ')