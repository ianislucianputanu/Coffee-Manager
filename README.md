# Coffee Manager — Sistem de comandă și gestiune stoc pentru cafenele

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
- Actualizare automată a stocului după fiecare vânzare
- Raport zilnic automat cu vânzări, încasări și stoc rămas

## Cui i se adresează
Cafenele, baruri, fast-food-uri mici sau standuri care vor un sistem simplu 
de gestiune comenzi + stoc, fără costurile unui POS comercial complex.

## Stack tehnic
Python, Tkinter (GUI), gestiune date persistentă pentru stoc și vânzări.
