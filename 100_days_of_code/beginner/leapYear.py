class LeapYear:
    def __init__(self) -> None:
        pass
    
    def check_if_leap_year(self):
        year = int(input("Enter the year: "))
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print("Its a Leap Year")
        else:
            print("Its not a Leap Year")
                        
LeapYear().check_if_leap_year()