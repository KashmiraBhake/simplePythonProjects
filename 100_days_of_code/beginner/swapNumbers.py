import time
class SwapNumbers:
    def __init__(self, num1, num2) -> None:
        self._num1 = num1
        self._num2 = num2
    
    @property
    def num1(self):
        return self._num1
    
    @num1.setter
    def num1(self, num1):
        if not isinstance(num1,int):
            raise ValueError('Input must be an integer')
    
    @property
    def num2(self):
        return self._num2
    
    @num2.setter
    def num2(self, num2):
        if not isinstance(num2,int):
            raise ValueError('Input must be an integer')
        
    def swap_with_two_variables(self):
        start_time = time.time()
        print(f'The numbers are n1 = {self._num1} and n2 = {self._num2}')
        self._num2, self._num1 = self._num1, self._num2
        print(f'The numbers are n1 = {self._num1} and n2 = {self._num2}')
        end_time = time.time()
        self._calculate_execution_time(start_time,end_time)
    
    def swap_with_extra_variables(self):
        start_time = time.time()
        print(f'The numbers are n1 = {self._num1} and n2 = {self._num2}')
        temp_var = self._num1 
        self._num1 = self._num2
        self._num2 = temp_var
        print(f'The numbers are n1 = {self._num1} and n2 = {self._num2}')
        end_time = time.time()
        self._calculate_execution_time(start_time,end_time)
    
    def swap_using_aritmatic_operations(self):
        start_time = time.time()
        print(f'The numbers are n1 = {self._num1} and n2 = {self._num2}')
        self._num1 = self._num1 + self._num2
        self._num2 = self._num1 - self._num2
        self._num1 = self._num1 - self._num2
        print(f'The numbers are n1 = {self._num1} and n2 = {self._num2}')
        end_time = time.time()
        self._calculate_execution_time(start_time,end_time)
        
    
    def _calculate_execution_time(self, t1, t2):
        print(f'Time of execution is {t2-t1:.20f}')
    
SwapNumbers(3000000,211111).swap_using_aritmatic_operations()
SwapNumbers(3000000,211111).swap_with_extra_variables()
SwapNumbers(3000000,211111).swap_with_two_variables()
    