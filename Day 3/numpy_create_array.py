import numpy as np

arr = []

a = int(input("Enter an integer value: "))

b = int(input("Enter an integer value: "))

c = int(input("Enter an integer value: "))

d = int(input("Enter an integer value: "))

e = int(input("Enter an integer value: "))


arr = np.append(arr, [a, b, c, d, e])

print(arr)


# Size of array * size of one array element
print("The memory size of array is {} bytes".format(arr.size * arr.itemsize))