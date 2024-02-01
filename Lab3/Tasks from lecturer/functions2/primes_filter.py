def filter_prime(lst):
    prime_lst = []
    for i in lst:
        is_prime = True
        if i <= 1:
            continue
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            prime_lst.append(i)
    return prime_lst


print(filter_prime([-20, -19, -18, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
