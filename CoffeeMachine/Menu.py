from pythonProject.CoffeeMachine.MenuItem import MenuItem


class Menu:
    def __init__(self):
        self.menu = [MenuItem(name = 'latte', water = 200, cost = 2.5, milk = 150, coffee=20),
                     MenuItem(coffee = 10, water = 100, name = 'espresso', cost = 1.5, milk = 100),
                     MenuItem(cost = 0.5, milk = 50, name = 'cappuccino', coffee = 5, water = 50)]

    def get_items(self):
        options = ''
        for i in self.menu:
            options += f'{i.name}  ({i.cost})  / '

        return options

    def find_drink(self, order_name):
        for i in self.menu:
            if i.name == order_name:
                return i

        return None
