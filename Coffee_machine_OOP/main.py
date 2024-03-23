from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
machine_on = True

while machine_on:
    coffee = input(f"Choose your coffee: {menu.get_items()}      ")
    user_coffee = menu.find_drink(coffee)
    if coffee_maker.is_resource_sufficient(user_coffee):
        if money_machine.make_payment(user_coffee.cost):
            coffee_maker.make_coffee(user_coffee)
    if input("Do you want to continue? y/n").lower() == "n":
        machine_on = False
