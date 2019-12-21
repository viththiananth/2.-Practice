import string

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

import numpy as np

np_weight = np.array(weight_kg)
print(np_weight)

a = np.array([[1, 2, 3], [4, 5, 6]], dtype='float')
print(a)

# Reshaping 3X4 array to 2X2X3 array
arr = np.array([[1, 2, 3, 4],
                [5, 2, 4, 2],
                [1, 2, 0, 1]])

newarr = arr.reshape(3, 2, 2)

print("\nOriginal array:\n", arr)
print("Reshaped array:\n", newarr)

c = np.zeros((3, 3))
print(c)

d = np.full((3, 3), 6)
print(d)

e = 10 * np.random.random((3, 3))
print(e)

f = np.arange(0, 30, 5)
print(f)

my_array=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(my_array)

temp=my_array[:2,:2]
print(temp)

temp1=my_array[[0,0,1],[0,0,2]]
print(temp1)

conditional_array=my_array>1
temp3=my_array[conditional_array]
print(temp3)


i=np.array([[1,2,3,4,5],[4,5,6,7,7]])
print(i)


j=i+1
k=i-1
l=i*2
m=i/2
n=i**2

print(j,"\n")
print(k,"\n")
print(l,"\n")
print(m,"\n")
print(n,"\n")



arr11 = np.array([[1, 5, 6],
                [4, 7, 2],
                [3, 1, 9]])

print("Row-wise maximum elements raw wise:",arr11.max(axis=0))
print ("Row-wise maximum elements coloumn wise:", arr11.max(axis = 1))

print(arr11.max())

print(arr11.sum())

print('Coloumn wise Sum:',arr11.sum(axis=0))
print('Raw wise Sum :',arr11.sum(axis=1))

print(arr11[[0,1],[0,2]])

f=np.arange(0,36,1)
g=f.reshape(1,6,6)
print(g)

print(g[::7])