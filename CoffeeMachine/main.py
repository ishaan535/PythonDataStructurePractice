from pythonProject.CoffeeMachine.CoffeeMaker import CoffeeMaker
from pythonProject.CoffeeMachine.Menu import Menu
from pythonProject.CoffeeMachine.MoneyMachine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}")
    if choice == "Off":
        is_on = False
    elif choice == "report":
        coffeeMaker.report()
        moneyMachine.report()
    else:
        drink = menu.find_drink(choice)
        if coffeeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
            coffeeMaker.make_coffee(drink)