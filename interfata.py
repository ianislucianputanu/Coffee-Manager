import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import date
import os

from cafenea import Cafe
from date import MENIU, STOC, NUME_INGREDIENTE, UNITATI

CULORI={
    "fundal": "#f8f7f5",
    "card": "#ffffff",
    "card_hover": "#f0eefb",
    "accent": "#534AB7",
    "accent_deschis": "#534AB7",
    "alb": "#222222",
    "gri": "#aaaaaa",
    "rosu": "#E24B4A",
    "cos_fundal": "#f0eefb",
}

FONTURI={
    "titlu": ("Arial", 18, "bold"),
    "card_nume": ("Arial", 12, "bold"),
    "card_pret": ("Arial", 11),
    "cos": ("Arial", 12),
    "cos_total": ("Arial", 16, "bold"),
    "buton": ("Arial", 11, "bold"),
    "mic": ("Arial", 10),
}

cafe=Cafe(MENIU, STOC, NUME_INGREDIENTE)
cantitati={key: 0 for key in MENIU}
poze_cache={}
vanzari_zi = {}

def preincarca_poza():
    for key, produs in MENIU.items():
        nume=produs["nume"]
        dosar=os.path.join("poze", f"{nume}.png")
        try:
            poza=Image.open(dosar)
            poza=poza.resize((160, 120), Image.LANCZOS)
            poze_cache[key]= ImageTk.PhotoImage(poza)
        except:
            poze_cache[key]= None
    
def actualizeaza_cos():
    for widget in frame_cos.winfo_children():
        widget.destroy()
    items=cafe.cart.items
    if not items:
        tk.Label(
            frame_cos,
            text="Cosul este gol",
            font=FONTURI["cos"],
            fg = CULORI["gri"],
            bg=CULORI["cos_fundal"]
        ).pack(anchor="w", pady=4)
    else:
        for nume, data in items.items():
            subtotal=data["pret"]*data["qty"]
            rand=tk.Frame(frame_cos, bg=CULORI["cos_fundal"])
            rand.pack(fill="x", pady=3)
            tk.Label(
                rand,
                text=f"x{data['qty']}",
                font=FONTURI["mic"],
                fg=CULORI["alb"],
                bg=CULORI["accent"],
                padx=6,
                pady=2
            ).pack(side="left")

            tk.Label(
                rand,
                text=f"{nume}",
                font=FONTURI["cos"],
                fg=CULORI["alb"],
                bg=CULORI["cos_fundal"]
            ).pack(side="left")

            tk.Label(
                rand,
                text=f"{subtotal} RON",
                font=FONTURI["cos"],
                fg=CULORI["accent_deschis"],
                bg=CULORI["cos_fundal"]
            ).pack(side="right")

        tk.Frame(
            frame_cos,
            bg=CULORI["gri"],
            height=1
        ).pack(fill="x", pady=8)

        rand_total=tk.Frame(frame_cos, bg=CULORI["cos_fundal"])
        rand_total.pack(fill="x")

        tk.Label(
            rand_total,
            text="Total",
            font=FONTURI["cos"],
            fg=CULORI["accent_deschis"],                
            bg=CULORI["cos_fundal"]
        ).pack(side="left")

        tk.Label(
            rand_total,
            text=f"{cafe.cart.total()} RON",                
            font=FONTURI["cos_total"],
            fg=CULORI["alb"],
            bg=CULORI["cos_fundal"]
        ).pack(side="right")

def actualizeaza_meniu():
    for widget in frame_grila.winfo_children():
        widget.destroy()
    for key, produs in MENIU.items():
        ok, _ = cafe.check_stock(produs, 1)
        card = tk.Frame(
            frame_grila,
            bg=CULORI["card"],
            cursor="hand2" if ok else "arrow"
        )

        index=int(key) - 1
        rand_grila = index // 3
        col_grila = index % 3

        card.grid(
            row=rand_grila,
            column=col_grila,
            padx=6,
            pady=6,
            sticky="nsew"
        )

        poza=poze_cache.get(key)
        if poza:
            label_poza = tk.Label(
                card,
                image=poza,
                bg=CULORI["card"]
            )
            label_poza.image=poza
            label_poza.pack()
            if not ok:
                label_poza.config(fg=CULORI["gri"])
        else:
            tk.Frame(
                card,
                bg=CULORI["gri"],
                width=160,
                height=120
            ).pack()

        tk.Label(
            card,
            text=produs["nume"],
            font=FONTURI["card_nume"],
            fg=CULORI["alb"] if ok else CULORI["gri"],
            bg=CULORI["card"],
            wraplength=150
        ).pack(pady=(8, 2), padx=8)
        
        if ok:
            tk.Label(
                card,
                text=f"{produs['pret']} RON",
                font=FONTURI["card_pret"],
                fg=CULORI["accent_deschis"],
                bg=CULORI["card"]
            ).pack(pady=(0,6))
        else:
            tk.Label(
                card,
                text="indisponibil",
                font=FONTURI["mic"],
                fg=CULORI["alb"],
                bg=CULORI["rosu"],
                padx=8,
                pady=3
            ).pack(pady=(0, 6))

        frame_qty = tk.Frame(card, bg=CULORI["card"])
        frame_qty.pack(pady=(0, 10))

        tk.Button(
            frame_qty,
            text="-",
            font=("Arial", 14),
            width=2,
            bg=CULORI["card_hover"],
            fg=CULORI["alb"],
            relief="flat",
            cursor="hand2",
            state="normal" if ok else "disabled",
            command=lambda k=key: scade(k)
        ).pack(side="left", padx=4)

        tk.Label(
            frame_qty,
            text=str(cantitati[key]),
            font=FONTURI["card_nume"],
            fg=CULORI["alb"],
            bg=CULORI["card"],
            width=2
        ).pack(side="left")

        tk.Button(
            frame_qty,
            text="+",
            font=("Arial", 14),
            width=2,
            bg=CULORI["accent"],
            fg=CULORI["alb"],
            relief="flat",
            cursor="hand2",
            state="normal" if ok else "disabled",
            command=lambda k=key: adauga(k)
        ).pack(side="left", padx=4)    

def adauga(key):
    produs=MENIU[key]
    qty_noua=cantitati[key]+1
    ok, missing=cafe.check_stock(produs, qty_noua)
    if not ok:
        messagebox.showwarning(
            "Stoc insuficient", "Nu mai avem stoc pentru acest produs!"
        )
        return
    cantitati[key]=qty_noua
    cafe.add_product(key, qty_noua)
    nume_produs=produs["nume"]
    cafe.cart.items[nume_produs]={
        "pret": produs["pret"],
        "qty": qty_noua
    }
    actualizeaza_meniu()
    actualizeaza_cos()

def scade(key):
    if cantitati[key]>0:
        cantitati[key]-=1
        produs=MENIU[key]
        nume_produs=produs["nume"]
        if cantitati[key] == 0:
            cafe.cart.items.pop(nume_produs, None)
        else:
            cafe.cart.items[nume_produs] = {
                "pret": produs["pret"],
                "qty": cantitati[key]
            }
        actualizeaza_meniu()
        actualizeaza_cos()

def finalizeaza_comanda():
    if not cafe.cart.items:
        messagebox.showinfo("Cos gol", "Nu ai selectat niciun produs!")
        return
    total=cafe.cart.total()
    confirmat=messagebox.askyesno(
        "Confirmare",
        f"Total de plata: {total} RON\nConfirmi comanda?"
    )
    if confirmat:
        for nume, data in cafe.cart.items.items():
            if nume in vanzari_zi:
                vanzari_zi[nume]["qty"] += data["qty"]
            else:
                vanzari_zi[nume] = {
                    "pret": data["pret"],
                    "qty": data["qty"]
                }
        for key, qty in cantitati.items():
            if qty>0:
                cafe.inventory.consume(MENIU[key]["ingrediente"], qty)
        cafe.cart.items={}
        for key in cantitati:
            cantitati[key]=0

        actualizeaza_meniu()
        actualizeaza_cos()
        messagebox.showinfo("Comanda plasata!", "Multumim! Comanda ta a fost inregistrata.")

def goleste_cosul():
    cafe.cart.items={}
    for key in cantitati:
        cantitati[key]=0
    actualizeaza_meniu()
    actualizeaza_cos()

def genereaza_raport():
    nume_fisier=f"raport_{date.today()}.txt"
    stoc=cafe.inventory.stock

    with open(nume_fisier, "w", encoding="utf-8") as f:
        f.write(f"RAPORT {date.today()}\n")
        f.write("=" * 30 + "\n\n")

        f.write("PRODUSE VANDUTE:\n")
        if vanzari_zi:
            for nume, data in vanzari_zi.items():
                total_produs=data["pret"] * data["qty"]
                f.write(f"   - {nume} x{data['qty']}: {total_produs} RON\n")
        else:
            f.write("  (nimic vandut)\n")

        total_zi=sum(d["pret"]*d["qty"] for d in vanzari_zi.values())
        f.write(f"\n TOTAL INCASAT: {total_zi} RON\n\n")
        f.write("STOC RAMAS:\n")
        for ing, cant in stoc.items():
            nume_ing=NUME_INGREDIENTE.get(ing, ing)
            unitate=UNITATI.get(ing, "")
            f.write(f" - {nume_ing}: {cant} {unitate}\n")

def inchidere():
    genereaza_raport()
    fereastra.destroy()

fereastra = tk.Tk()
fereastra.title("Cafenea")
fereastra.geometry("560x750")
fereastra.config(bg=CULORI["fundal"])
fereastra.resizable(False, False)

header=tk.Frame(fereastra, bg=CULORI["accent"], pady=16)
header.pack(fill="x")

tk.Label(
    header,
    text="Cafenea",
    font=FONTURI["titlu"],
    bg=CULORI["accent"],
    fg="#ffffff"
).pack()

tk.Label(
    header,
    text="Bun venit! Alege ce doresti",
    font=FONTURI["mic"],
    bg=CULORI["accent"],
    fg="#CECBF6"
).pack()

canvas=tk.Canvas(
    fereastra,
    bg=CULORI["fundal"],
    highlightthickness=0
)
scrollbar=tk.Scrollbar(
    fereastra,
    orient="vertical",
    command=canvas.yview
)
frame_scroll=tk.Frame(canvas, bg=CULORI["fundal"])
frame_scroll.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=frame_scroll, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

tk.Label(
    frame_scroll,
    text="MENIU",
    font=FONTURI["mic"],
    fg=CULORI["gri"],
    bg=CULORI["fundal"]
).pack(anchor="w", padx=16, pady=(12, 4))

frame_grila=tk.Frame(frame_scroll, bg=CULORI["fundal"])
frame_grila.pack(padx=10, pady=4)

for i in range(3):
    frame_grila.columnconfigure(i, weight=1)

frame_cos_container=tk.Frame(
    frame_scroll,
    bg=CULORI["cos_fundal"],
    pady=14
)
frame_cos_container.pack(fill="x", padx=10, pady=10)

tk.Label(
    frame_cos_container,
    text="COSUL TAU",
    font=FONTURI["mic"],
    fg=CULORI["gri"],
    bg=CULORI["cos_fundal"]
).pack(anchor="w", padx=16, pady=(0, 8))

frame_cos=tk.Frame(frame_cos_container, bg=CULORI["cos_fundal"])
frame_cos.pack(fill="x", padx=16)
frame_butoane=tk.Frame(frame_cos_container, bg=CULORI["cos_fundal"])
frame_butoane.pack(fill="x", padx=16, pady=(12, 0))

tk.Button(
    frame_butoane,
    text="Goleste cosul",
    font=FONTURI["buton"],
    bg=CULORI["card_hover"],
    fg=CULORI["gri"],
    relief="flat",
    padx=14,
    pady=8,
    cursor="hand2",
    command=goleste_cosul
).pack(side="left")

tk.Button(
    frame_butoane,
    text="Finalizeaza comanda",
    font=FONTURI["buton"],
    bg=CULORI["accent"],
    fg="#ffffff",
    relief="flat",
    padx=16,
    pady=8,
    cursor="hand2",
    command=finalizeaza_comanda
).pack(side="right")

preincarca_poza()

actualizeaza_meniu()
actualizeaza_cos()
fereastra.protocol("WM_DELETE_WINDOW", inchidere)
fereastra.mainloop()