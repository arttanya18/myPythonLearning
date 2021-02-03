MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

money = {"money": 0}


# TODO: 1. Print report of all coffee machine report.


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money['money']}")


def print_turnoff():
    print("Turn Off Coffee Machine. Bye.")


def deduction(coffee_type):
    """ Input coffee type. Deduct resources """
    if resources['water'] >= MENU[coffee_type]["ingredients"]["water"] and \
            resources['milk'] >= MENU[coffee_type]["ingredients"]["milk"] and \
            resources['coffee'] >= MENU[coffee_type]["ingredients"]["coffee"]:
        resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
        resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
        resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
        return True
    else:
        print("Resources (water/milk/coffee) are not enough")
        return False


def coin_check(quarter, dime, nickel, penny, price, ordering):
    total_coin = (quarter * 0.25) + (dime * 0.1) + (nickel * 0.05) + (penny * 0.01)
    if total_coin < price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif total_coin >= price and deduction(ordering):
        money['money'] += price
        change = total_coin - price
        if change != 0:
            print(f"Here is ${change:.2f} dollars in change.")
            print(f"Here is your {ordering}. ☕️ Enjoy.")
            return True
        else:
            print(f"Here is your {ordering}. ☕️ Enjoy.")
            return True


def coffeeMachine():
    should_continue = True
    while should_continue:
        order = input("What would you like? (espresso/latte/cappuccino): ")
        if order == "report":
            print_report()
        elif order == "off":
            print_turnoff()
            should_continue = False
        else:
            coffee_cost = MENU[order]['cost']
            print("Please insert coin.")
            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickels = float(input("How many nickels?: "))
            pennies = float(input("How many pennies?: "))
            coin_ok = True
            coin_ok = coin_check(quarters, dimes, nickels, pennies, coffee_cost, order)
            # print(coin_ok)
            if coin_ok:
                deduction(order)


coffeeMachine()

# TODO: 2. Check all resources sufficient?

# TODO: 3. Process coins.

# TODO: 4. Check transaction successful?

# TODO: 5. Make Coffee

