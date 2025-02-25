class MenuItem:
    def __init__(self, name, cost, water, milk, coffee):
        self.name = name
        self.cost = cost
        self.ingredients = {'water': water, 'milk':milk , 'coffee':coffee }

    def __str__(self):
        return self.name