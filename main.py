'''


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
                if ptr[i] not in words_up and ptr[i][0] in 'ЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮQWERTYUIOPLKJHGFDSAZXCVBNM':
                    words_up.append(ptr[i])
                words.append(ptr[i])
print(words)
print(words_uniq)
print(words_up)
words_for_words = []
for i in range(len(words_uniq)):
    ind = words.index(words_uniq[i])
    wrd = words[ind:]
    while words_uniq[i] in wrd:
        wrd.remove(words_uniq[i])
    words_for_words.append(wrd)
print(words_for_words)
count_ptrs = 0
with open('output.txt', 'w', encoding='utf8') as f_out:
    while count_ptrs != ptrs:
        ind_1 = randint(0, len(words_up) - 1)
        word_1 = words_up[ind_1]
        word = word_1
        sentence = word_1
        count_wrds = 0
        while word[-1] not in '.?!' or count_wrds > 20:
            ind = words_uniq.index(word)
            ind_new = randint(0, len(words_for_words[ind]) - 1)
            word = words_for_words[ind][ind_new]
            sentence += word
            count_wrds += 1
        count_ptrs += 1

