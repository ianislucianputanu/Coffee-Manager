from inventory import Inventory

class Cafe:
    def __init__(self, meniu, nume_ingrediente):
        self.meniu = meniu
        self.nume_ingrediente = nume_ingrediente
        self.inventory = Inventory()
        self.total_vanzari = 0

    def show_menu(self):
        print("\n--- MENIU ---")
        for k, v in self.meniu.items():
            print(f"{k}. {v['nume']} - {v['pret']} RON")

    def show_stock(self):
        print("\n--- STOC ---")
        for ing, qty in self.inventory.stock.items():
            print(f"{self.nume_ingrediente[ing]}: {qty}")

    def check_stock(self, product):
        return self.inventory.check(product["ingrediente"])

    def pay(self, price):
        while True:
            try:
                money = float(input("Introdu bani: "))
                if money < price:
                    print("Bani insuficienti")
                else:
                    return money
            except:
                print("Valoare invalida")

    def prepare(self, key):
        product = self.meniu[key]

        ok, missing = self.check_stock(product)

        if not ok:
            print(f" Lipseste: {self.nume_ingrediente[missing]}")
            return

        print(f"\n Pret: {product['pret']} RON")
        money = self.pay(product["pret"])

        self.inventory.consume(product["ingrediente"])
        self.total_vanzari += product["pret"]

        print(f"Se prepara {product['nume']}...")
        print("Gata!")
        print(f"Rest: {money - product['pret']:.2f}")