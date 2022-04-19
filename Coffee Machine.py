
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def checking_resources(drink_choice):
    """Will check if the machine has enough resources to make the drink user requested."""
    for elements in MENU[drink_choice]["ingredients"]:
        if MENU[drink_choice]["ingredients"][elements] > resources[elements]:
            print(f"Sorry, there is not enough {elements}.")
            return False
        else:
            return True


def checking_money(total, drink_choice):
    if total >= MENU[drink_choice]["cost"]:
        return True
    else:
        print("Sorry, that is not enough money. Money refunded.")


def calculate_change(total, drink_choice):
    if total > MENU[drink_choice]["cost"]:
        return total - MENU[drink_choice]["cost"]
    else:
        return


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
}

money = 0
coffee_on = True
while coffee_on:
    # TODO: Prompt user what they would like - espresso, latte, cappuccino
    drink_choice = input("What would you like to drink? (espresso / latte / cappuccino): ").lower()
    # TODO: Turn off the coffee machine by entering "off" to the prompt
    if drink_choice == "off":
        coffee_on = False
    # TODO: Print report by entering "report" to the prompt
    elif drink_choice == "report":
        report()
    # TODO: The program should check if the resources are sufficient
    elif drink_choice == "espresso" or drink_choice == "latte" or drink_choice == "cappuccino":
        checking_resources(drink_choice)
    # TODO: User will insert coins and the program must process and calculate the total amount.
        if checking_resources(drink_choice):
            print("Please insert coins.")
            num_quarters = float(input("How many quarters?: "))
            num_dimes = float(input("How many dimes?: "))
            num_nickels = float(input("How many nickels?: "))
            num_pennies = float(input("How many pennies?: "))
            total = (num_quarters * 0.25) + (num_dimes * 0.10) + (num_nickels * 0.05) + (num_pennies * 0.01)
        # TODO: Check if the transaction was successful. Update the money in the report and offer change if necessary.
            checking_money(total, drink_choice)
            if checking_money(total, drink_choice):
                money += MENU[drink_choice]["cost"]
                print(f"Here is ${calculate_change(total, drink_choice)} in change.")
                # TODO: Update the resources report after the coffee is made.
                for elements in MENU[drink_choice]["ingredients"]:
                    resources[elements] -= MENU[drink_choice]["ingredients"][elements]
                print(f"Here is your {drink_choice}. Enjoy!")


