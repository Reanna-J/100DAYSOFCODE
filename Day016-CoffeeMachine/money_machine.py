class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0

    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        print("Please insert coins.")
        total = 0

        for coin in self.COIN_VALUES:
            count = int(input(f"How many {coin}?: "))
            total += count * self.COIN_VALUES[coin]

        return total

    def make_payment(self, cost):
        payment = self.process_coins()

        if payment >= cost:
            change = round(payment - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False