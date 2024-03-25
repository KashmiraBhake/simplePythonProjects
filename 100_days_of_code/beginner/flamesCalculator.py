class FLAMESCalculator:
    def __init__(self) -> None:
        self.flames = {'F':'Friendship','L':'Love','A':'Affair','M':'Marriage','E':'Enemy','S':'Siblings'}
        self.flame_keys = ['F','L','A','M','E','S']
        self.len_flames = len(self.flame_keys)
        
        
    def calculate_flames(self):
        name1,name2 = self._get_input()
        for letter1 in name1[:]: 
            if letter1 in name2:
                name1.remove(letter1)
                name2.remove(letter1)
        total_len = len(name1)+len(name2)
        
        while self.len_flames >1:
            pos = total_len % self.len_flames
            self.flame_keys = self._set_pointer(pos)
            self.len_flames -=1
        
        print(f'FLAMES Relationship between the two is of {self.flames[self.flame_keys[0]]}')
    
    def _set_pointer(self,pos):
        if pos == 0:
            return self.flame_keys[:pos-1] 
        elif pos > 1:
            return self.flame_keys[pos:]+self.flame_keys[:pos-1] 
        else:
            return self.flame_keys[pos:]
        
    def _get_input(self):
        name1 = list(input("Enter the first name: ").strip().lower().replace(' ', ''))
        name2 = list(input("Enter the second name: ").strip().lower().replace(' ', ''))
        return name1,name2

FLAMESCalculator().calculate_flames()