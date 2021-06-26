import numpy as np

arr = []

# number of elements the user wants to input
number = int(input("Enter number of integer elements you want to input: "))

for i in range(0, number):
    element = int(input([]))
    arr=np.append(arr,element)


print(arr)


# Size of array * size of one array element
print("The memory size of array is {} bytes".format(arr.size * arr.itemsize))