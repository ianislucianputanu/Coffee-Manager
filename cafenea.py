from inventory import Inventory
from cart import Cart

class Cafe:
    def __init__(self, meniu, stoc, nume_ing):
        self.meniu = meniu
        self.inventory = Inventory(stoc)
        self.cart = Cart()
        self.nume_ing = nume_ing

    def show_menu(self):
        print("\n--- MENIU ---")
        for k, v in self.meniu.items():
            print(f"{k}. {v['nume']} - {v['pret']} lei")

    def check_stock(self, produs, qty):
        return self.inventory.check(produs["ingrediente"], qty)

    def add_product(self, key):
        if key not in self.meniu:
            print("Produs invalid")
            return False

        produs = self.meniu[key]

        qty = int(input("Introduceți cantitatea: "))

        ok, missing = self.check_stock(produs, qty)

        if not ok:
            print(f" Indisponibil: {self.nume_ing[missing]}")
            return False

        self.cart.add(produs, qty)

        print(f" {produs['nume']} x{qty} adaugat in cos")
        return True

    def checkout(self):
        total = self.cart.total()

        print(f"\n TOTAL: {total} lei")

        money = self.pay(total)

        
        for name, data in self.cart.items.items():
            for key, produs in self.meniu.items():
                if produs["nume"] == name:
                    self.inventory.consume(produs["ingrediente"], data["qty"])

        print("\n BON FINAL")
        self.cart.show()

        print(f"\n Rest: {money - total:.2f}")

    def pay(self, price):
        while True:
            try:
                money = float(input("Introdu bani: "))
                if money < price:
                    print("Bani insuficienți")
                else:
                    return money
            except:
                print("Valoare invalidă")