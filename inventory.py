class Inventory:
    def __init__(self):
        self.stock = {
            "cafea_g": 200,
            "apa_ml": 1000,
            "lapte_ml": 500,
            "pudra_cacao_g": 100,
            "pliculet_ceai_buc": 5
        }

    def check(self, ingredients):
        for ing, qty in ingredients.items():
            if self.stock.get(ing, 0) < qty:
                return False, ing
        return True, None

    def consume(self, ingredients):
        for ing, qty in ingredients.items():
            self.stock[ing] -= qty