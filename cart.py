class Cart:
    def __init__(self):
        self.items = {}  
        

    def add(self, produs, qty):
        name = produs["nume"]

        if name in self.items:
            self.items[name]["qty"] += qty
        else:
            self.items[name] = {
                "pret": produs["pret"],
                "qty": qty
            }

    def total(self):
        return sum(v["pret"] * v["qty"] for v in self.items.values())

    def show(self):
        print("\n--- COȘ ---")
        if not self.items:
            print("Coș gol")
            return

        for name, data in self.items.items():
            print(f"{name} x{data['qty']} = {data['pret'] * data['qty']} lei")

        print("TOTAL:", self.total(), "lei")