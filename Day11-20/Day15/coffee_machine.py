# COFFEE MACHINE PROGRAM
# Prompts user to choose a drink (espresso/latte/cappuccino)
# If user types report then print the available resources
# If the user types espresso/latte/cappuccino the check if avaiable resources meet requirements for the drink if not then print Sorry....
# If the resources are available process the coins inserted, if not then print Sorry...
# If everything works well then dispense the drink
# if "off" is typed then end the program

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def user_prompt():
    """Formats and prints the initial message on console"""
    return input("What would you like? (espresso/latte/cappuccino): ")


def print_report(machine_resources):
    """Prints existing state of coffee machine resources"""
    print(f"Water: {machine_resources['water']}ml")
    print(f"Milk: {machine_resources['milk']}ml")
    print(f"Coffee: {machine_resources['coffee']}g")
    print(f"Money: ${machine_resources['money']}")


def check_resources(user_input, machine_resources):
    """Determines if the drink can be prepared with existing resources"""
    if MENU[user_input]["ingredients"]["water"] > machine_resources["water"]:
        print("Sorry there is not enough water.")
        return False
    elif MENU[user_input]["ingredients"]["coffee"] > machine_resources["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    elif user_input != "espresso":
        if MENU[user_input]["ingredients"]["milk"] > machine_resources["milk"]:
            print("Sorry there is not enough milk.")
            return False
    else:
        return True


def adjust_resources(user_input, machine_resources):
    """Adjusts current resources based on drink"""
    if user_input == "espresso":
        machine_resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        machine_resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
    elif user_input == "latte":
        machine_resources["water"] -= MENU["latte"]["ingredients"]["water"]
        machine_resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
        machine_resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
    else:
        machine_resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        machine_resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
        machine_resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]

    return machine_resources



def process_coins(user_input, machine_resources):
    """Asks user for how many of each coins inserted and calculates balance"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total_coins = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    if MENU[user_input]["cost"] > total_coins:
        print("Sorry that's not enough money. Money refunded.")
        return
    else:
        balance = total_coins - MENU[user_input]["cost"]
        machine_resources["money"] += MENU[user_input]["cost"]
        if balance > 0:
            print(f"Here is ${round(balance, 2)} in change")
        print(f"Here is your {user_input} Enjoy!")
    return machine_resources


def machine():
    """Main function that controls the entire loop"""
    #copying global resources to another variable
    machine_resources = resources
    while True:
        user_input = user_prompt()
        if user_input == "off":
            print("Shutting down the machine....")
            return
        elif user_input == "report":
            print_report(machine_resources)
        else:
            if check_resources(user_input, machine_resources) is False:
                continue
            if process_coins(user_input, machine_resources) is None:
                continue
            adjust_resources(user_input, machine_resources)



machine()

