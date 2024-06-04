class Machine:
    def __init__(self):
        self.resources ={
            "water":500,
            "milk":300,
            "coffee":100,
        }
    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def enough_resources(self , order):
        can_make = True
        for item in order.ingredients:
            if self.resources[item] < order.ingredients[item]:
                print(f"Not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self,order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Your {order.name} is done!")