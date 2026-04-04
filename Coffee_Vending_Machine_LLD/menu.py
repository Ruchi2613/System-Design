'''3. The machine should have a menu to display the available coffee options and their prices.
'''
class CoffeeMenu:
    def __init__(self):
        self.menu = {
            "Espresso": 2.5,
            "Cappuccino": 3.0,
            "Latte": 3.5
        }

    def display_menu(self):
        print("Coffee Menu:")
        for coffee, price in self.menu.items():
            print(f"{coffee}: ${price:.2f}")
