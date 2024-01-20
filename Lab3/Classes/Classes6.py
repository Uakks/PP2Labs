lst = [1, 2, 3, 4, 5, 12, 13, 15, 16, 17, 18, 19, 20]
print(list(filter(lambda x: all(x % i != 0 for i in range(2, int(x))) and x != 1, lst)))
