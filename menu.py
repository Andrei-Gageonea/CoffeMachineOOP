class MenuItem:
    def __init__(self,name,cost,water,milk,coffee):
        self.name = name
        self.cost = cost
        self.ingredients = {'water': water , 'milk':milk , 'coffee':coffee}

class Menu:

    def __init__(self):
        self.menu = [
            MenuItem(name="espresso" , water = 50, coffee = 20 , milk = 0 , cost= 1.5),
            MenuItem(name="cappuccino" , water = 250, coffee = 24 , milk = 50 , cost= 3),
            MenuItem(name="latte", water=200, coffee=24, milk=150, cost=2.5),
        ]

    def get_items(self):
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_item(self , order):
        for item in self.menu:
            if item.name == order:
                return item
        print("The selected item is unavailable")
        return False
