from csv import DictReader

def read(csv_file):
    try:
        try:
            return DictReader(open(csv_file))

        except FileNotFoundError:
            print("Wrong file or file path")
            raise
    except OSError:
        print("Wrong type")
        raise 

