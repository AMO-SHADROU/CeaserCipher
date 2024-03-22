import data
import art

money = 0


def show_menu():
    user_choice = input("What would you like: {espresso, latte, cappuccino}?   ").lower()
    return user_choice


def report():
    print(data.resources)
    print(f"Money: ${money}")


def check_resources(coffe):
    for ingredient in data.MENU[coffe]["ingredients"].keys():
        if data.MENU[coffe]["ingredients"][ingredient] > data.resources[ingredient]:
            print(f"Sorry dont have enough {ingredient}!")
            return False
        else:
            data.resources[ingredient] -= data.MENU[coffe]["ingredients"][ingredient]
    return True


def coin():
    print("Insert coin here ")
    penny = int(input("Enter how many penny?\n")) * 0.01
    nickel = int(input("Enter how many nickel?\n")) * 0.05
    dime = int(input("Enter how many dime?\n")) * 0.1
    quarter = int(input("Enter how many quarter?\n")) * 0.25
    total = penny + nickel + dime + quarter
    return total


machine_on = True

while machine_on:
    print(art.logo)
    coffe_choice = show_menu()
    if coffe_choice == "report":
        report()
    elif coffe_choice == "off":
        exit()
    elif coffe_choice in data.MENU.keys():
        if check_resources(coffe_choice):
            user_coin = coin()
            coffe_cost = data.MENU[coffe_choice]["cost"]
            if user_coin > coffe_cost:
                print(f"Here is your change: {round(user_coin - coffe_cost, 2)}")
                print("Enjoy your coffe!☕")
            else:
                print("Sorry not enough money!")
                exit()
    should_continue = input("Do you want to continue? y/n  ").lower()
    if should_continue == "n":
        machine_on = False
