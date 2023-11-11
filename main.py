'''
Group:
Varfolomeeva Viktoria
Sineokaya Anastasiya 55
'''

from random import randint

words_uniq = []
words = []
words_up = []

with open('input.txt', encoding='utf8') as f_in:
    ptrs = int(f_in.readline())
    for x in f_in:
        if x != ptrs:
            ptr = x.split()
            for i in range(len(ptr)):
                if ptr[i] not in words_uniq:
                    words_uniq.append(ptr[i])
                letters = 'ЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮQWERTYUIOPLKJHGFDSAZXCVBNM'
                if ptr[i] not in words_up and ptr[i][0] in letters:
                    words_up.append(ptr[i])
                words.append(ptr[i])

words_for_words = []

for i in range(len(words_uniq)):
    ind = words.index(words_uniq[i])
    wrd = words[ind:]
    while words_uniq[i] in wrd:
        wrd.remove(words_uniq[i])
    words_for_words.append(wrd)

count_ptrs = 0

with open('output.txt', 'w', encoding='utf8') as f_out:
    while count_ptrs != ptrs:
        ind_1 = randint(0, len(words_up) - 1)
        word_1 = words_up[ind_1]
        word = word_1
        sentence = word_1
        count_wrds = 0

        while word[-1] not in '.?!' and count_wrds <= 20:
            ind = words_uniq.index(word)
            while not words_for_words[ind]:
                ind = randint(0, len(words_uniq) - 1)

            ind_new = randint(0, len(words_for_words[ind]) - 1)
            word = words_for_words[ind][ind_new]
            sentence += ' ' + word
            count_wrds += 1

        print(sentence, file=f_out)
        count_ptrs += 1
