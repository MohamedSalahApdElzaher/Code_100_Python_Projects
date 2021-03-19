# import some classes
from menu import MenuItem, Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# initialize objects
moneyMachine = MoneyMachine()
coffeeMaker = CoffeeMaker()
menu = Menu()

# program work flow
is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        moneyMachine.report()
        coffeeMaker.report()
    else:
        drink = menu.find_drink(choice)
        if coffeeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
            coffeeMaker.make_coffee(drink)

# good bay message
print("Thanks For Using Coffee Machine :)")

 
