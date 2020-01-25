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