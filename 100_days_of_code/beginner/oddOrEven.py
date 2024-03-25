class OddOrEven:
    def __init__(self) -> None:
        pass
    
    def check_odd_or_even(self):
        num = int(input("Enter the number: "))
        if num % 2 == 0:
            print("Number is even")
        else:
            print("Number is odd")

OddOrEven().check_odd_or_even()