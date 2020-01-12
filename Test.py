def myfunc1(*args):
    result=''
    for i in range(0,len(args)):
        if i%2==0:
            result+=args[i].upper()
        else:
            result+=args[i].lower()
    print(result)

myfunc1('My Name')