# Coffee-Manager
## Descriere proiect
Acest proiect reprezintă o aplicație de tip self-service pentru o cafenea, similară cu sistemele de comandă întâlnite în restaurantele fast-food (McDonald's, KFC etc.).
Aplicația permite utilizatorului să selecteze produse dintr-un meniu vizual, să aleagă cantitatea dorită, să le adauge într-un coș și să finalizeze comanda printr-un proces intuitiv.
## •	Fiecare produs este definit prin ingrediente
## •	Stocul conține materii prime (cafea, lapte, apă)
## •	În momentrul în care se încarcă meniul:
-	se verifică dacă există suficiente ingrediente
- dacă NU → produsul devine indisponibil
## • Produsele sunt adăugate în coș
## • La finalizarea comenzii:
- se confirmă plata
- se actualizează stocul
- se înregistrează vânzările
### La închiderea aplicației se generează automat un fișier: raport_YYYY-MM-DD.txt, care conține produsele vândute, totalul încasat, stocul rămas.
## Interfață grafică (GUI)
Aplicația include o interfață realizată cu Tkinter, care simulează o tabletă de comandă:
-	Produse afișate cu imagini
-	Butoane pentru modificarea cantității
-	Coș actualizat în timp real
-	Produse marcate ca indisponibile dacă nu există stoc
-	Buton de finalizare comandă
-	Mesaje interactive (confirmări, erori)
## Funcționalități principale
-	Vizualizare meniu produse
-	Selectare cantitate pentru fiecare produs
- Coș de cumpărături dinamic
- Verificare stoc ingrediente în timp real
- Afișare produse indisponibile
-	Checkout (plată simulată)
- Generare bon final
- Generare raport zilnic automat
- Gestionare stoc ingrediente


