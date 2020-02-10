def make_pretty(func):
    def inner_func():
        print("I got decorated")
        func()
    return (inner_func)

#def ordinary():
#    print("I am ordinary")
#pretty=make_pretty(ordinary)

#print(pretty())

@make_pretty
def ordinary():
    print("I am ordinary")

print(ordinary())


