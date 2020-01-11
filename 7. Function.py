def myfunc(*args):
    this_list=[];
    for x in args:
        if x%2==0:
            this_list.append(x)
    print(this_list)
    return(this_list)



myfunc(1,2,3,4,5,6)



def is_even(x):
    if x%2==0:
        print(True)
    else:
        print(False)

is_even(12)



def myfunc1(my_string):
    result=''
    for i in range(0,len(my_string)):
        if i%2==0:
            result+=my_string[i].upper()
        else:
            result+=my_string[i].lower()
    print(result)

myfunc1('Viththi')