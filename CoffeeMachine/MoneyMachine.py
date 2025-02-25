class MoneyMachine:
    coin_values = {'quarters':0.25, 'dimes':0.10, 'nickel':0.05, 'pennies':0.01}
    currency = '$'
    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f"Amount: {self.currency}{self.profit:.2f}")

    def make_payment(self, cost):
        self.money_received = 0
        print("Please insert coins.")

        for key, value in self.coin_values.items():
            self.money_received += int(input(f"Please enter the number of {key}: ")) * value
            if self.money_received >= cost:
                break

        if self.money_received >= cost:
            change = self.money_received - cost
            if change > 0:
                print(f"Here is {self.currency}{change:.2f} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Insufficient money. Money refunded.")
            self.money_received = 0
            return False