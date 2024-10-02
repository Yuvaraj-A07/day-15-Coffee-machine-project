MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
# print(MENU["latte"]["ingredients"]["water"])
next = True
water = resources["water"]
milk = resources["milk"]
coff = resources["coffee"]
total = 0
amount = 0
while (next):
    coffee = input("What would you like? (espresso/latte/cappuccino):")
    if coffee == "off":
        next = False
    if coffee == "report":
        print("Water : ", water, "ml")
        print("Milk : ", milk, "ml")
        print("coffee : ", coff, "g")
        print("Moneys :$", round(amount, 1))

    if coffee == "latte" or coffee == "cappuccino" or coffee == "espresso":
        # print(MENU[coffee]["ingredients"]["water"])
        if water < MENU[coffee]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        elif milk < MENU[coffee]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
        elif coff < MENU[coffee]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
        else:
            print("Please insert coins.")

            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))

            total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
            if (total >= MENU[coffee]["cost"]):
                change = total - MENU[coffee]["cost"]
                water = water - MENU[coffee]["ingredients"]["water"]
                milk = milk - MENU[coffee]["ingredients"]["milk"]
                coff = coff - MENU[coffee]["ingredients"]["coffee"]
                amount = amount + MENU[coffee]["cost"]
                if (change > 0):
                    print("Here is $", round(change, 2), "in change.")
                print("Here is your ", coffee, "☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        # else:
        #   print("Sorry there is not enough ingredients.")
