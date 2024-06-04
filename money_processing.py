class MoneyMachine:
    CURRENCY = "€"
    MONEY_TYPES = {
        "10 euro cent": 0.1,
        "50 euro cent": 0.5,
        "1 euro": 1,
        "2 euro":2
    }
    def __init__(self):
        self.profit = 0
        self.money_recieved = 0

    def report(self):
        print(f"Money: {self.profit}{self.CURRENCY}")

    def process_money(self):
        print("Please insert money.")
        for item in self.MONEY_TYPES:
            self.money_recieved += int(input(f"How many {item} coins?")) * self.MONEY_TYPES[item]
        return self.money_recieved

    def payment(self , cost):
        self.process_money()
        if self.money_recieved >= cost:
            change = round(self.money_recieved - cost , 2)
            print(f"Here is {self.money_recieved - cost}{self.CURRENCY} in change.")
            self.profit += cost
            self.money_recieved = 0
            return True
        else:
            print("You do not have enough money. Payment returned.")
            self.money_recieved = 0
            return False