# Coffee Manager — Sistem de comandă și gestiune stoc pentru cafenele
## Demo
   [YouTube](https://youtu.be/bggshjONOZA)

## Ce rezolvă
Multe cafenele mici gestionează stocul manual sau deloc, produsele se vând 
și după ce ingredientele s-au terminat iar la final de zi nimeni nu știe 
exact cât s-a încasat sau ce a mai rămas pe stoc.

Coffee Manager rezolvă asta printr-o interfață tip self-service (similară 
McDonald's/KFC) conectată direct la un sistem de stoc bazat pe rețete:
fiecare produs "știe" din ce ingrediente e făcut, iar stocul se actualizează
automat la fiecare vânzare.

## Funcționalități
- Meniu vizual cu produse și imagini (interfață Tkinter, stil tabletă)
- Fiecare produs definit prin rețetă (ingrediente + cantități)
- Verificare automată a stocului: produsele fără ingrediente suficiente 
  devin indisponibile instant
- Coș de cumpărături dinamic, cu ajustare cantitate
- Checkout cu plată simulată și bon de comandă
- Actualizare stoc direct din interfață, proprietarul poate seta cantitățile disponibile la începutul zilei/evenimentului, fără cunoștințe tehnice sau acces la cod
- Raport zilnic automat cu vânzări, încasări și stoc rămas

## Cui i se adresează
Cafenele, baruri, fast-food-uri mici sau standuri care vor un sistem simplu 
de gestiune comenzi + stoc, fără costurile unui POS comercial complex.

**De reținut**: Coffee Manager este un instrument de gestiune comenzi și stoc, **nu un înlocuitor al casei de marcat fiscale** (obligatorie legal pentru orice vânzare). Funcționează cel mai bine ca sistem complementar, proprietarul vede în timp real ce se vinde și ce stoc mai are, în paralel cu sistemul fiscal existent. Stocul introdus se resetează la fiecare pornire a aplicației (gândit pentru sesiuni de o zi/eveniment, nu pentru urmărire pe termen lung între zile diferite).

## Stack tehnic
Python, Tkinter (GUI), gestiune date persistentă pentru stoc și vânzări.
