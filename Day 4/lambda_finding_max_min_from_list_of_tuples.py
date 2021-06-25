# list containing 3 tuples
list_one = [("Hillary", 22), ('Kihara', 31), ('Lydia', 30), ('Ben', 33)]

# Find tuple with max value
max_value_tuple = max(list_one, key=lambda x:x[1])

# Find tuple with lowest value
min_value_tuple = min(list_one, key=lambda x:x[1])

print("The tuple containing the maximum value is: {}".format(max_value_tuple))

print("The tuple containing the minimum value is: {}".format(min_value_tuple))