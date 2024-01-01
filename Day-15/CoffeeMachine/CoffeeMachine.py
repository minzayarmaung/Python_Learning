from game_data import MENU
import art

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Original Resources

water_resource = resources['water']
milk_resource = resources['milk']
coffee_resource = resources['coffee']

# Accessing data for Coffees
# Espresso Data

espresso_data = MENU.get('espresso')
espresso_water = espresso_data['ingredients']['water']
espresso_coffee = espresso_data['ingredients']['coffee']
espresso_cost = espresso_data['cost']

# Latte Data

latte_data = MENU.get('latte')
latte_water = latte_data['ingredients']['water']
latte_milk = latte_data['ingredients']['milk']
latte_coffee = latte_data['ingredients']['coffee']
latte_cost = latte_data['cost']

# Cappuccino Data

cappuccino_data = MENU.get('cappuccino')
cappuccino_water = cappuccino_data['ingredients']['water']
cappuccino_milk = cappuccino_data['ingredients']['milk']
cappuccino_coffee = cappuccino_data['ingredients']['coffee']
cappuccino_cost = cappuccino_data['cost']

# Coin Prices
quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01


def process_coin(coffee_cost, coffee):
    global profit
    print("Please insert coins.")
    quarters_amount = int(input("How many coins of quarters ? :"))
    dimes_amount = int(input("How many coins of dimes? :"))
    nickles_amount = int(input("How many coins of nickles? :"))
    pennies_amount = int(input("How many coins of pennies? :"))

    total_Amount = ((quarters * quarters_amount) +
                    (dimes * dimes_amount) +
                    (nickles * nickles_amount) +
                    (pennies * pennies_amount))

    # Checking the Payment Amount
    if total_Amount == coffee_cost:
        profit += coffee_cost
        return f"Here is your {coffee} ☕. Enjoy ! 🤗"
    elif total_Amount > coffee_cost:
        change = int(total_Amount - coffee_cost)
        profit += coffee_cost
        return (f"Here is ${change} dollars in change."
                f"Here is your {coffee} ☕. Enjoy ! 🤗")
    else:
        return "Sorry , that's not enough money. Money Refunded."


def report():
    water_amount = resources["water"]
    milk_amount = resources["milk"]
    coffee_amount = resources["coffee"]
    total_profit = profit
    return (f"Water : {water_amount}\nMilk : {milk_amount}\n"
            f"Coffee : {coffee_amount}\nProfit : ${total_profit} dollars")


def startGame():
    while True:

        decision = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if decision == "report":
            print(report())
        elif decision == "off":
            print("The Coffee Machine is Turned Off. ☕")
            return False

        # LATTE CHECK
        elif decision == "latte":
            coffee_type = decision
            print(f"You have chosen : {decision}")
            # Checking Enough Resource or Not
            if (resources['water'] >= latte_water and
                    resources['milk'] >= latte_milk and
                    resources['coffee'] >= latte_coffee):
                resources['water'] -= latte_water
                resources['milk'] -= latte_milk
                resources['coffee'] -= latte_coffee

                # Passing the argument to process the Payment
                print(process_coin(latte_cost, coffee_type))
            else:
                if resources['water'] < latte_water:
                    print(f"Sorry , there is not enough water.")
                elif resources['milk'] < latte_milk:
                    print(f"Sorry , there is not enough milk.")
                elif resources['coffee'] < latte_coffee:
                    print(f"Sorry , there is not enough coffee.")

        # ESPRESSO COFFEE CHECK
        elif decision == "espresso":
            coffee_type = decision
            print(f"You have chosen : {decision}")
            # Checking Enough Resource or Not
            if (resources['water'] >= espresso_water and
                    resources['coffee'] >= espresso_coffee):

                resources['water'] -= espresso_water
                resources['coffee'] -= espresso_coffee

                # Passing the argument to process the Payment
                print(process_coin(espresso_cost, coffee_type))

            else:
                if resources['water'] < espresso_water:
                    print(f"Sorry , there is not enough water.")
                elif resources['coffee'] < espresso_coffee:
                    print(f"Sorry , there is not enough coffee.")

        # CAPPUCCINO COFFEE CHECK
        elif decision == "cappuccino":
            coffee_type = decision
            print(f"You have chosen : {decision}")
            # Checking Enough Resource or Not
            if (resources['water'] >= cappuccino_water and
                    resources['milk'] >= cappuccino_milk and
                    resources['coffee'] >= cappuccino_coffee):

                resources['water'] -= cappuccino_water
                resources['milk'] -= cappuccino_milk
                resources['coffee'] -= cappuccino_coffee

                # Passing the argument to process the Payment
                print(process_coin(cappuccino_cost, coffee_type))
            else:
                if resources['water'] < cappuccino_water:
                    print(f"Sorry , there is not enough water.")
                elif resources['milk'] < cappuccino_milk:
                    print(f"Sorry , there is not enough milk.")
                elif resources['coffee'] < cappuccino_coffee:
                    print(f"Sorry , there is not enough coffee.")


print(art.logo)
startGame()
