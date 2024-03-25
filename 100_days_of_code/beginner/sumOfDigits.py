class SumOfDigits:
    def __init__(self) -> None:
        self._num = abs(int(input("Enter the digit to be added \n")))
    
    def calculate_sum(self):
        sum = 0
        while self._num > 0:
            sum += self._num % 10
            self._num = self._num // 10
        return sum


print(SumOfDigits().calculate_sum())