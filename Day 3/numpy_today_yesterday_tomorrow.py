import numpy as np

# today
today = np.datetime64('today', 'D')
print("Today is {}".format(today))

# tomorrow
print("Tomorrow is {}".format(today+1))

# yesterday
print("Yesterday was {}".format(today-1))

