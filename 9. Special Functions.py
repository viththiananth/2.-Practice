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
    zipped=zip(word1,word2)
    lst=[]
    for w1,w2 in zipped:
        x=((w1+connector+w2))
        lst.append(x)
    print(lst)
concatenate(['A','a'],['B','b'],'-')


def concatenate_short(word1,word2,connector):
    result=(L1+connector+L2 for (L1,L2) in zip(word1,word2))
    print (result)

a=concatenate_short(['A','B'],['a','b'],'-')
print(a)


def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function()

def display():
    print('I Am Viththiananth')

a=decorator_function(display)
print(a())