from cafenea import Cafe
from date import MENIU, STOC, NUME_INGREDIENTE

cafe = Cafe(MENIU, STOC, NUME_INGREDIENTE)

while True:
    print("\n1. Meniu")
    print("2. Adauga produs")
    print("3. Vezi cos")
    print("4. Checkout")
    print("0. Exit")

    opt = input("> ")

    if opt == "1":
        cafe.show_menu()

    elif opt == "2":
        cafe.show_menu()
        key = input("Alege produs: ")
        cafe.add_product(key)

    elif opt == "3":
        cafe.cart.show()

    elif opt == "4":
        cafe.checkout()

    elif opt == "0":
        print("Vă mai așteptăm!")
        break