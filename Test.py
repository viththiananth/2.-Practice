class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account Owner Name: {self.owner}\nAccount Balance :   ${self.balance}'

    def deposit(self, dep_amount):
        self.balance += dep_amount
        print (f'{dep_amount} got deposited to your account. Your account balance is {self.balance}')

    def withdraw(self, wit_amount):
        if wit_amount > self.balance:
            print ('You have insufficient Account Balance')
        else:
            self.balance -= wit_amount
            print (f'You withdrawed {wit_amount} and your current account balance is {self.balance}')


Jose = Account('Jose', 150)
Jose.deposit(1000)
Jose.withdraw(500)

print(Jose)


