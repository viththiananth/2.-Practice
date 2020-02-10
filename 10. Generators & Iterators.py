def square(N):
    for i in range(N):
        yield i ** 2


for x in square(10):
    print(x)
