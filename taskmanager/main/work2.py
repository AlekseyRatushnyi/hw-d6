# import re
#
# bad_words = ['редиска']
#
# mytext = 'Не хороший человек - Редиска! '
#
# index = mytext.lower().find(bad_words[0])
# print(index)
# new_text = mytext.replace(bad_words[0][1:], "*" * (len(bad_words[0])-1))
# print(new_text)

bad_words = ['редиска', 'картошка']


def censor(value):
    for i in range(len(bad_words)):
        num_index = value.lower().find(bad_words[i])
        if num_index > 0:
            value = value.replace(bad_words[i][1:], "*" * (len(bad_words[i]) - 1))
    return value


value = 'Не хороший человек - редиска! или Картошка!!'
print(censor(value))
