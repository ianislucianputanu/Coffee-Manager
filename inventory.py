class Inventory:
    def __init__(self, stoc):
        self.stock = stoc.copy()

    def check(self, ingrediente, qty):
        for ing, cant in ingrediente.items():
            if self.stock.get(ing, 0) < cant * qty:
                return False, ing
        return True, None

    def consume(self, ingrediente, qty):
        for ing, cant in ingrediente.items():
            self.stock[ing] -= cant * qty