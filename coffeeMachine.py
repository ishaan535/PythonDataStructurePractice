class Coffee:
    def __init__(self, drink_name, water, milk, powder, cost):
        self.drink_name = drink_name
        self.water = water
        self.milk = milk
        self.powder = powder
        self.cost = cost

    def get_drink_name(self):
        return self.drink_name

    def get_water(self):
        return self.water

    def get_milk(self):
        return self.milk

    def get_powder(self):
        return self.powder

    def get_cost(self):
        return self.cost


class CoffeeMachine:
    water = 400
    milk = 540
    powder = 120
    money = 0.0

    espresso = Coffee("Espresso", 50, 0, 18, 1.50)
    latte = Coffee("Latte", 200, 150, 24, 2.50)
    cappuccino = Coffee("Cappuccino", 250, 100, 24, 3.00)


    def print_report(self):
        print(f"Water: {CoffeeMachine.water} ml")
        print(f"Milk: {CoffeeMachine.milk} ml")
        print(f"Coffee: {CoffeeMachine.powder} g")
        print(f"Money: ${CoffeeMachine.money:.2f}")


    def check_resources(drink_name):
        if drink_name == "espresso":
            if CoffeeMachine.water < CoffeeMachine.espresso.get_water():
                print("Insufficient water.")
                return False
            if CoffeeMachine.powder < CoffeeMachine.espresso.get_powder():
                print("Insufficient coffee.")
                return False
        elif drink_name == "latte":
            if CoffeeMachine.water < CoffeeMachine.latte.get_water():
                print("Insufficient water.")
                return False
            if CoffeeMachine.milk < CoffeeMachine.latte.get_milk():
                print("Insufficient milk.")
                return False
            if CoffeeMachine.powder < CoffeeMachine.latte.get_powder():
                print("Insufficient coffee.")
                return False
        elif drink_name == "cappuccino":
            if CoffeeMachine.water < CoffeeMachine.cappuccino.get_water():
                print("Insufficient water.")
                return False
            if CoffeeMachine.milk < CoffeeMachine.cappuccino.get_milk():
                print("Insufficient milk.")
                return False
            if CoffeeMachine.powder < CoffeeMachine.cappuccino.get_powder():
                print("Insufficient coffee.")
                return False
        return True


    def process_coins(self):
        print("Please insert coins.")
        quarters = int(input("No. of quarters: ")) * 0.25
        dimes = int(input("No. of dimes: ")) * 0.10
        nickels = int(input("No. of nickels: ")) * 0.05
        pennies = int(input("No. of pennies: ")) * 0.01
        return quarters + dimes + nickels + pennies


    def make_coffee(drink_name):
        if not CoffeeMachine.check_resources(drink_name):
            return
        if drink_name == "espresso":
            cost = CoffeeMachine.espresso.get_cost()
        elif drink_name == "latte":
            cost = CoffeeMachine.latte.get_cost()
        elif drink_name == "cappuccino":
            cost = CoffeeMachine.cappuccino.get_cost()
        inserted_money = CoffeeMachine.process_coins()
        if inserted_money < cost:
            print("Insufficient money. Money refunded.")
            return
        if drink_name == "espresso":
            CoffeeMachine.water -= CoffeeMachine.espresso.get_water()
            CoffeeMachine.powder -= CoffeeMachine.espresso.get_powder()
        elif drink_name == "latte":
            CoffeeMachine.water -= CoffeeMachine.latte.get_water()
            CoffeeMachine.milk -= CoffeeMachine.latte.get_milk()
            CoffeeMachine.powder -= CoffeeMachine.latte.get_powder()
        elif drink_name == "cappuccino":
            CoffeeMachine.water -= CoffeeMachine.cappuccino.get_water()
            CoffeeMachine.milk -= CoffeeMachine.cappuccino.get_milk()
            CoffeeMachine.powder -= CoffeeMachine.cappuccino.get_powder()
        CoffeeMachine.money += cost
        if inserted_money > cost:
            print(f"Here is ${inserted_money - cost:.2f} in change.")
        print(f"Here is your {drink_name}. Enjoy!")


def main():
    while True:
        print("Select your item")
        print("1. Espresso")
        print("2. Latte")
        print("3. Cappuccino")
        print("4. Report")
        print("5. Exit")
        choice = int(input())
        if choice == 1:
            CoffeeMachine.make_coffee("Espresso")
        elif choice == 2:
            CoffeeMachine.make_coffee("Latte")
        elif choice == 3:
            CoffeeMachine.make_coffee("Cappuccino")
        elif choice == 4:
            CoffeeMachine.print_report()
        elif choice == 5:
            break
        else:
            print("Invalid selection, please try again.")


if __name__ == "__main__":
    main()
