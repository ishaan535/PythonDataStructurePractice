class CoffeeMaker:
    def __init__(self):
        self.resources = {'water': 1000, 'milk': 500, 'coffee': 500}

    def report(self):
        for key,value in self.resources.items():
            print(f"{key.capitalize()}: {value}ml" if key != "coffee" else f"{key.capitalize()}: {value}g")

    def is_resource_sufficient(self, drink):
        for key, value in drink.ingredients.items():
            if value > self.resources.get(key, 0):
                print(f"Insufficient {key}.")
                return False
        return True

    def make_coffee(self, order):
        if self.is_resource_sufficient(order):
            for key, value in order.ingredients.items():
                self.resources[key] -= value
            print(f"Here is your {order.name}.")