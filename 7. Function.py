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


def myfunc2(args):
    index=0
    result=''
    for i in args:
        if index%2==0:
            result+=i.upper()
        else:
            result+=i.lower()
        index+=1
    print(result)

myfunc2('Viththi')


def less_of_two_even(a,b):
    if (a%2==0 and b%2==0):
        print(min(a,b))
    else:
        print(max(a,b))

less_of_two_even(5,4)


def old_macdonald(name):
    a = name[:3].capitalize()
    b = name[3:].capitalize()
    print(a+b)


old_macdonald('macdonald')

def master_yoda(text):
    a=text.split()[::-1]
    print(a)

master_yoda('How are you')


def almost_three(n):
    print((abs(100-n)<=10)or (abs(200-n)<=10))

almost_three(12)
almost_three(92)
almost_three(150)
almost_three(209)



def has_33(nums):
    for i in range(0,len(nums)):
        if nums[i:i+2]==[3,3]:
            True
        else:
            False

has_33(1,3,4,4,3,3)


def paper_doll(string):
    result=''
    for i in string:
        result+=i*3
    print(result)



paper_doll('viththi')

def find_33(nums):
    for x in range(0, len(nums)):
        if (nums[x] == 3 and nums[x + 1] == 3):
            print(True)
        else:
            print(False)


find_33([1, 2, 3, 4, 4, 3, 3])



def summer_69(arr):
    total=0
    add=True
    for x in arr:
        while add:
            if x!=6:
                total+=x
                break
            else:
                add=False
        while not add:
            if x!=9:
                break
            else:
                add=True
                break
    print(total)


summer_69([4,5,6,7,8,9,10])


def myfunc3(*args):
    result=''
    for i in range(0,len(args[0])):
        if i%2==0:
            result+=args[0][i].upper()
        else:
            result+=args[0][i].lower()
    print(result)

myfunc3('MyName')




        def count_prime(nums):
            prime = [2]
            x = 3
            if nums < 2:  # for the case of num = 0 or 1
                return 0
            while x <= nums:
                for y in range(3, x, 2):
                    if x % y == 0:
                        x += 2
                        break
                else:
                    prime.append(x)
                    x += 2
            print(prime)

        count_prime(100)
