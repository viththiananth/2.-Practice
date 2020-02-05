def word_length(phrase):
    print(list(map(len,phrase.split())))
word_length('I am Viththi')

import functools
def digits_to_number(digits):
    print(functools.reduce (lambda x,y:x*10+y,digits))
digits_to_number([1,2,3])

def filter_word(word_list,letter):
    filter_list=(filter(lambda word:word[0]==letter,word_list))
    return (filter_list)

l=['Viththi','Huawei']
filter_word(l,'H')


def concatenate(word1,word2,connector):
    zipped=zip()