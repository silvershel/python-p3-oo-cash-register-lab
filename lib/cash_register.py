#!/usr/bin/env python3

class CashRegister:

    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.last_transaction = None

    def add_item(self, title, price, quantity=1):
        self.items.extend([title] * quantity)
        # Think about a cash register. Adding an item wouldn't add more titles to the list, it would update the quantity.
        # In this case he get_items logic might change to returning the title "x" times based on the quantity.
        self.total += price * quantity
        self.last_transaction = (title, price, quantity)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
            print("There is no discount to apply.")

    def get_items(self):
        return [item for item in self.items]
    
    def void_last_transaction(self):
        if self.last_transaction:
            title, price, quantity = self.last_transaction
            for _ in range(quantity):
                self.items.remove(title)
            self.total -= price * quantity