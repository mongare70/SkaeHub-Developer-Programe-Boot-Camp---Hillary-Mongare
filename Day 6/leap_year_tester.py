def leap_year_tester(year):
    try: 
        if year%4 == 0 and year%400 == 0 or year%100 != 0:
            return True
        
        else: 
            return False
    except TypeError:
        print("Wrong type")
        raise
