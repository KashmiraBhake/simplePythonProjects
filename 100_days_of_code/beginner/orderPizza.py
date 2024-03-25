class OrderPizza:
    def __init__(self) -> None:
        self.toppings_menu = {"Paneer": 20, "Capsicum": 12, "Tomato": 10, 
                              "Soya Chunks": 15, "Pepparoni": 35, "Chicken": 40, 
                              "Cheese": 30, "Corn": 5}
        self.size_menu = {"Regular": 90, "Medium": 150, "Large": 200}
        self.base_menu = {"Pan Pizza": 2, "Thin Crust": 3, "Hand Tossed": 1, "Cheese Burst": 4}
    
    def make_your_pizza(self):
        base,size,toppings = self._get_inputs()
        pizza_price = self.size_menu[size.title()] * self.base_menu[base.title()]
        for top in toppings:
            pizza_price+=self.toppings_menu[top.title()]
        print(f"Your total is: Rs.{pizza_price}")
    
    def _get_inputs(self):
        base = input(f"Select the pizza base '{'/'.join(self.base_menu)}': ")
        size = input(f"Select the pizza size '{'/'.join(self.size_menu)}': ")
        is_ok = True
        toppings = []
        while is_ok:
            curr_topping =  input(f"Select the pizza topping '{'/'.join(self.toppings_menu)}': ")
            is_done = input("If selection is complete say Y/N: ")
            toppings.append(curr_topping)
            if is_done == 'Y':
                is_ok = False
        return base,size,toppings

OrderPizza().make_your_pizza()