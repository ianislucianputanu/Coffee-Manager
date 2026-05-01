class Cart:
    def __init__(self):
        self.items = []

    def add(self, produs):
        self.items.append(produs)

    def total(self):
        return sum(p["pret"] for p in self.items)

    def show(self):
        print("\n--- COȘ ---")
        for p in self.items:
            print(f"{p['nume']} - {p['pret']} lei")
        print("TOTAL:", self.total(), "lei")