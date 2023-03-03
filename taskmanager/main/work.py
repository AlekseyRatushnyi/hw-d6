
bad_words = ['редиска']


def lower(value):
    original = value.split()
    for n, i in enumerate(original):
        if i.lower() in bad_words:
            original[n] = i[0] +  "*" * (len(i) -1)
    return (' ').join(original)


mytext = 'Не хороший человек - редиска!'

print(lower(mytext))