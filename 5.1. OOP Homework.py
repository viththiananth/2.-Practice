import math

class Cylinder:
    def __init__(self,r,h):
        self.r=r
        self.h=h

    def volume(self):
        print(math.pi*self.r**2*self.h)

    def area(self):
        print(math.pi*self.r**2*self.h+2*math.pi*self.r*self.h)

cy=Cylinder(7,8)

cy.volume()
cy.area()


class Line(object):
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def length(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        print (((y2 ** 2 - y1 ** 2) - (x2 ** 2 - x1 ** 2)) * 1 / 2)

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        print (y2 - y1) / (x2 - x1)


coordinate1 = (1, 1)
coordinate2 = (3, 3)

li = Line(coordinate1, coordinate2)

li.length()


import math

class Cylinder:
    def __init__(self,r,h):
        self.r=r
        self.h=h

    def volume(self):
        return(math.pi*self.r**2*self.h)

    def area(self):
            return(math.pi*self.r**2*self.h+2*math.pi*self.r*self.h)

cy=Cylinder(7,8)

cy.volume()




class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account Owner Name: {self.owner}\nAccount Balance :   ${self.balance}'

    def deposit(self, dep_amount):
        self.balance += dep_amount
        return (f'{dep_amount} got deposited to your account. Your account balance is {self.balance}')

    def withdraw(self, wit_amount):
        if wit_amount > self.balance:
            return 'You have insufficient Account Balance'
        else:
            self.balance -= wit_amount
            return f'You withdrawed {wit_amount} and your current account balance is {self.balance}'


Jose = Account('Jose', 50)



###########Encapasulation###########
class Computuer:
    def __init__(self):
        self.__maxprice=900

    def sell(self):
        print('Selling Price is {}'.format(self.__maxprice))

    def SetMaxPrice(self,price):
        self.__maxprice=price

c=Computuer()
c.sell()

c.__maxprice=2000
c.sell()

c.SetMaxPrice(1200)
c.sell()



class ComplexNumber:
    def __init__(self,r=0,i=0):
        self.real=r
        self.img=i

    def getData(self):
        print("{0}+{1}j".format(self.real,self.img))

c1=ComplexNumber(1,2)
c1.getData()

c2=ComplexNumber(5)
c2.attri=12
c2.getData()
print(c2.real,c2.img,c2.attri)



class Dog():
    def __init__(self,name,type,flur):
        self.name=name
        self.type=type
        self.flur=flur

Sam=Dog('Viththi','Ananth',True)

print(Sam.type)



class book:
    def __init__(self,book,author,pages):
        self.book=book
        self.author=author
        self.pages=pages
        #print('{}'.format(self.book))
#    def __str__(self):
#        return ('Book : {}, Author : {}'.format(self.book,self.author))
    def __del__(self):
        pass

    def __len__(self):
        return self.pages

b=book('python','Jose',100)

len(b)


a=[1,2,3]
b=[4,5,6]
c=[7,8,9]
print(map(lambda x,y,z:x+y+z,a,b,c))

lst=range(10)
even=list(filter(lambda num:num%2==0,lst))
greater_than_three=list((filter(lambda num:num>3,lst))

print(even)