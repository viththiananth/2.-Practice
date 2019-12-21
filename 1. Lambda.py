mynums=[1,2,3,4,5]

print (list(map(lambda x:x**2,mynums)))

print(list(filter(lambda x:x%2==0,mynums)))

print(list(filter(lambda x:x%3==0,mynums)))

mynames=('Andy','Viththi','Arnold')

print(list(map(lambda x:x[0],mynames)))