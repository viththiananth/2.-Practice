from collections import Counter

lst = [1,2,2,2,2,3,3,3,1,2,1,12,3,2,32,1,21,1,223,1]

print(Counter(lst))


print(Counter('aabsbsbsbhshhbbsbs'))

s = 'How many times does each word show up in this sentence word times each each word'

words = s.split()
print(Counter(words))

c = Counter(words)

print(c.most_common(2))
print(sum(c.values()))
print(list(c))
print(set(c))
print(dict(c))
print(c.items())


#Default Dictionary
from collections import defaultdict
d ={}
d=defaultdict(object)
d['One','two','Three']

for i in d:
    print (i)

#Ordered Dictionary
from collections import OrderedDict

d = {}
d['a']="A"
d['b']="B"
d['d']="D"
d['c']="C"
d['e']="E"

print(d)

d1=OrderedDict()
d1['a']="A"
d1['b']="B"
d1['d']="D"
d1['c']="C"
d1['e']="E"