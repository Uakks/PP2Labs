def word_frequency(string):
    dictionary = dict()
    for i in string:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary.update({i: 1})

    return dictionary


print(word_frequency('abcdef'))
