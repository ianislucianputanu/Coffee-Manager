from cafenea import Cafe
from date import MENIU, NUME_INGREDIENTE

cafe = Cafe(MENIU, NUME_INGREDIENTE)

while True:
    print("\n1. Meniu")
    print("2. Comanda")
    print("3. Stoc")
    print("0. Exit")

    opt = input("> ")

    if opt == "1":
        cafe.show_menu()

    elif opt == "2":
        cafe.show_menu()
        choice = input("Alege: ")
        if choice in MENIU:
            cafe.prepare(choice)

    elif opt == "3":
        cafe.show_stock()

    elif opt == "0":
        print("Va mai asteptam!")
        break