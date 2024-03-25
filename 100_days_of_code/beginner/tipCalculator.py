class TipCalculator:
    def __init__(self) -> None:
        print("Welcome to the tip calculator!")
    
    def calculate_tip(self):
        bill, tip_perc, num = self._get_information_from_user()
        bill_with_tip = bill * (1 + (tip_perc/100))
        bill_per_person = bill_with_tip/num
        print(f"Your total bill including the tip is: Rs.{round(bill_with_tip,2)}")
        print(f"Each diner must pay: Rs.{round(bill_per_person,2)}")
    
    def _get_information_from_user(self):
        bill = float(input("What is the total bill amount? Rs."))
        tip_perc = float(input("What percentage tip would you like to give? %"))
        num = int(input("No. Of people dining: "))
        return bill, tip_perc, num

TipCalculator().calculate_tip()