
def summer_69(arr):
    total=0
    add=True
    for x in arr:
        while add:
            if x!=6:
                total+=x

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