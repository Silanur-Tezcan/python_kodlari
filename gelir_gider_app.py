import sqlite3
from tkinter import *
from tkinter import messagebox
from datetime import datetime

conn = sqlite3.connect("butce.db")
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tur TEXT NOT NULL,
    kategori TEXT NOT NULL,
    miktar REAL NOT NULL,
    tarih TEXT NOT NULL,
    aciklama TEXT
)
''')

conn.commit()
pencere = Tk()
pencere.title("Bütçem Yanımda")
pencere.geometry("400x500")
pencere.configure(bg="darkgray")

def veri_ekle():
    tur = var_tur.get()
    kategori = entry_kategori.get()
    miktar = entry_miktar.get()
    aciklama = entry_aciklama.get()
    tarih = datetime.now().strftime("%Y-%m-%d")

    if kategori == "" or miktar == "":
        messagebox.showwarning("Eksik Bilgi", "Lütfen tüm alanları doldur.")
        return

    try:
        miktar = float(miktar)
        cursor.execute("INSERT INTO transactions (tur, kategori, miktar, tarih, aciklama) VALUES (?, ?, ?, ?, ?)",
                       (tur, kategori, miktar, tarih, aciklama))
        conn.commit()
        messagebox.showinfo("Başarılı", f"{tur.title()} kaydedildi.")
        entry_kategori.delete(0, END)
        entry_miktar.delete(0, END)
        entry_aciklama.delete(0, END)
        ozet_goster()
    except ValueError:
        messagebox.showerror("Hata", "Miktar sayısal olmalı.")

def ozet_goster():
    cursor.execute("SELECT SUM(miktar) FROM transactions WHERE tur='gelir'")
    toplam_gelir = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(miktar) FROM transactions WHERE tur='gider'")
    toplam_gider = cursor.fetchone()[0] or 0

    bakiye = toplam_gelir - toplam_gider

    label_ozet.config(text=f"💰 Gelir: {toplam_gelir} TL\n💸 Gider: {toplam_gider} TL\n📌 Bakiye: {bakiye} TL")
var_tur = StringVar()
var_tur.set("gelir")

def verileri_temizle():
    if messagebox.askyesno("Onay", "Tüm verileri silmek istediğinize emin misiniz?"):
        cursor.execute("DELETE FROM transactions")
        conn.commit()
        messagebox.showinfo("Başarılı", "Tüm veriler temizlendi.")
        ozet_goster()

Label(pencere, text="Tür",fg="darkblue", font=("Arial", 15),bg="darkgray").pack()
OptionMenu(pencere, var_tur, "gelir", "gider").pack()

Label(pencere, text="Kategori",fg="darkblue",bg="darkgray").pack()
entry_kategori = Entry(pencere)
entry_kategori.pack()

Label(pencere, text="Miktar (TL)",fg="darkblue",bg="darkgray").pack()
entry_miktar = Entry(pencere)
entry_miktar.pack()

Label(pencere, text="Açıklama",fg="darkblue",bg="darkgray").pack()
entry_aciklama = Entry(pencere)
entry_aciklama.pack()

Button(pencere, text="Kaydet", command=veri_ekle).pack(pady=10)
label_ozet = Label(pencere, text="", font=("Arial", 12), fg="darkgreen",bg="darkgray")
label_ozet.pack(pady=20)
Button(pencere, text="Verileri Temizle", command=verileri_temizle).pack(pady=10)
ozet_goster()
pencere.mainloop()
