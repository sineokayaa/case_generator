'''


'''

from random import randint

words_uniq = []
words = ''

with open('input.txt') as f_in:
    ptrs = int(f_in.readline())
    for x in f_in:
        if x != ptrs:
            ptr = x.split()
            for i in range(len(ptr)):
                if ptr[i] not in words_uniq:
                    words_uniq.append(ptr[i])
                words += ptr[i]

words_for_words = []
for i in range(len(words_uniq)):
    ind = words.find(words_uniq[i])
    wrd = words[ind + len(words_uniq[i]):].split()
    while words_uniq[i] in wrd:
        wrd.remove(words_uniq[i])
    words_for_words.append(wrd)

for i in range(ptrs):
    ind_1
