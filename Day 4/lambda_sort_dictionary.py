orders = {
    'pizza':200,
    'potatoes':2000,
    'chicken':500,
    'soda':1000,
    'cake':100,
    'biscuits':200
    
}

# Sort orders dictionary by value (key=lambda x:x[1]) in ascending order (reverse=False)
sort_orders = sorted(orders.items(), key=lambda x:x[1], reverse=False)

# print sorted dictionary
for x,y in sort_orders:
    print(x, y)
