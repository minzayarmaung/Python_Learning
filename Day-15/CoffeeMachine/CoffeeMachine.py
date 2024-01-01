from game_data import MENU

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


def report():
    water_amount = resources["water"]
    milk_amount = resources["milk"]
    coffee_amount = resources["coffee"]
    return f"Water : {water_amount}\nMilk : {milk_amount}\nCoffee : {coffee_amount}"


def startGame():
    while True:

        decision = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if decision == "report":
            print(report())
        elif decision == "off":
            print("The Coffee Machine is Turned Off. ☕")
            return False

        elif decision == "latte":

            print(f"You have chosen : {decision}")

            # Checking Enough Resource or Not
            if (resources['water'] >= latte_water and
                    resources['milk'] >= latte_milk and
                    resources['coffee'] >= latte_coffee):

                resources['water'] -= latte_water
                resources['milk'] -= latte_milk
                resources['coffee'] -= latte_coffee
        else:
            print(f"Sorry , not Enough resources to make a {decision}")


startGame()
