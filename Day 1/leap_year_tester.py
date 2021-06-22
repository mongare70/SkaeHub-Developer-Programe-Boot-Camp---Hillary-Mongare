def leap_year_tester(year):
    if year%4 == 0 and year%400 == 0 or year%100 != 0:
        return True
    
    else: 
        return False

print(leap_year_tester(2000))

print(leap_year_tester(2400))

print(leap_year_tester(1800))

print(leap_year_tester(1900))

print(leap_year_tester(2100))

print(leap_year_tester(2200))

print(leap_year_tester(2300))

print(leap_year_tester(2500))
