mylist = [1, 2, 3]
myset = set()

print(type(myset))
print(type(mylist))

class MySample():
    pass

print(type(MySample))


class Dog():
    species = 'Mammal'
    def __init__(self,breed,name, spot):
        self.breed=breed
        self.name=name
        self.spot=spot
    def bark(self,number):
        print("WOOF!!!. My Name is {} & Number is {}".format(self.name,number))


my_dog=Dog('Viththi','Ananth',False)
print(my_dog)

print(my_dog.name)
print(my_dog.breed)
print(my_dog.species)
print(my_dog.bark(10))