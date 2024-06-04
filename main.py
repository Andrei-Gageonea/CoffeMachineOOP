from menu import Menu
from coffe_maker import Machine
from money_processing import MoneyMachine

menu = Menu()
machine = Machine()
money = MoneyMachine()

def is_working():
    choice = input("What woud you like?\n(espresso: 1.5€ / cappuccino: 3€ / latte: 2.5€)\n")
    order = menu.find_item(choice)
    if choice == "report":
        machine.report()
        money.report()
        is_working()
    elif choice == "off":
        return "Machine off"
    elif machine.enough_resources(order):
        if money.payment(order.cost):
            machine.make_coffee(order)
            is_working()

is_working()
