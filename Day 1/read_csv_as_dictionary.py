from csv import DictReader

data = DictReader(open('Day 1/data/peeps.csv'))

for row in data:
    print(row)