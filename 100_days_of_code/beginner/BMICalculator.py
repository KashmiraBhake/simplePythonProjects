class BMICalculator:
    def __init__(self, hight, weight) -> None:
        self._hight = hight
        self._weight = weight
        
    @property
    def hight(self):
        return self._hight
    
    @hight.setter
    def hight(self, hight):
        if not isinstance(hight, int) or isinstance(hight, float):
            raise ValueError('hight must be a numeric value')
        
    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, weight):
        if not isinstance(weight, int) or isinstance(weight, float):
            raise ValueError('weight must be a numeric value')
    
    def calculate_bmi(self):
        BMI =  self._weight/(self._hight**2)
        if BMI >= 30:
            return f'Your BMI is {BMI}. You fall under obese category.'
        elif 25 < BMI < 30:
            return f'Your BMI is {BMI}. You fall under overweight category.'
        elif 18.5 < BMI < 25:
            return f'Your BMI is {BMI}. You fall under healthy category.'
        else:
            return f'Your BMI is {BMI}. You fall under underweight category.'
            
            

print(BMICalculator(1.64, 89).calculate_bmi())