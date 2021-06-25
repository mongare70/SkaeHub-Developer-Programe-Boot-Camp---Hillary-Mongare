import itertools as it

# loop through iterable
def cycle_data(iterable):
    return it.cycle(iterable)

list_one = ['a', 'b', 'c', 'd', 'e']

# call cycle_data function
output = cycle_data(list_one)

# loop through 'output' variable
for i in output:
    print(i)
