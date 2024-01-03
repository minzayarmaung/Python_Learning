from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMaker = CoffeeMaker()
menu = Menu()
moneyMachine = MoneyMachine()
is_On = True

off_MESSAGE = "The Shop is Closed ! See you Tomorrow 👋🤗🤗"

while is_On:
    options = menu.get_items()
    choice = input(f"Welcome to Starbucks , Can I take your Order {options} : ")
    if choice == "off":
        print(off_MESSAGE)
        is_On = False
    elif choice == "report":
        coffeeMaker.report()
        moneyMachine.report()
    else:
        drink = menu.find_drink(choice)

        if coffeeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
            coffeeMaker.make_coffee(drink)
