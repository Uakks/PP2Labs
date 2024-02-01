def common_elements(lst1, lst2):
    common_elements = []
    for i in lst1:
        if i in lst2:
            common_elements.append(i)
            lst2.remove(i)

    return common_elements


print(common_elements([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 8]))
