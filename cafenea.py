from inventory import Inventory
from cart import Cart

class Cafe:
    def __init__(self, meniu, stoc, nume_ing):
        self.meniu = meniu
        self.inventory = Inventory(stoc)
        self.cart = Cart()
        self.nume_ing = nume_ing

    def check_stock(self, produs, qty):
        return self.inventory.check(produs["ingrediente"], qty)

    def add_product(self, key):
        if key not in self.meniu:
            return False, "Produs invalid"

        produs = self.meniu[key]
        ok, missing = self.check_stock(produs, qty)

        if not ok:
            return False, self.nume_ing[missing]

        self.cart.add(produs, qty)
        return True, produs

    def checkout(self):
        total = self.cart.total()
        
        for name, data in self.cart.items.items():
            for key, produs in self.meniu.items():
                if produs["nume"] == name:
                    self.inventory.consume(produs["ingrediente"], data["qty"])
        self.cart.items={}
        return total
