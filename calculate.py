from datetime import datetime

def string_to_date(input):
    return datetime.strptime(input, "%d/%m/%Y")

def check_date(input):
    if string_to_date(input) < datetime.strptime("01/01/1900", "%d/%m/%Y") or string_to_date(input) > datetime.strptime("31/12/2999", "%d/%m/%Y"):
        return False
    else:
        return True

def date_between(first_date, second_date):
    if check_date(first_date) and check_date(second_date):
        return abs(string_to_date(first_date) - string_to_date(second_date)).days - 1
    else:
        print("The valid date range is between 01/01/1900 and 31/12/2999")

if __name__ == "__main__":
    print(date_between("2/6/1983", "22/6/1983"))
    print(date_between("4/7/1984", "25/12/1984"))
    print(date_between("3/1/1989", "3/8/1983"))
