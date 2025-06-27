import tkinter as tk
from tkinter import messagebox
import os

class NotDefteri(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("📝 Python Not Defteri")
        self.geometry("450x350")
        self.configure(bg="#f0f0f0")

        # Başlık etiketi
        lbl_baslik = tk.Label(self, text="🗒️ Notunu Gir", font=("Helvetica", 14, "bold"), bg="#f0f0f0", fg="#333")
        lbl_baslik.pack(pady=10)

        # Not alanı
        self.txt_not = tk.Text(self, width=50, height=12, font=("Calibri", 11), bd=2, relief="groove", bg="white")
        self.txt_not.pack(pady=5)

        # Kaydet butonu
        self.btn_kaydet = tk.Button(
            self,
            text="💾 Kaydet",
            font=("Helvetica", 11, "bold"),
            bg="#4CAF50",
            fg="white",
            padx=10,
            pady=5,
            command=self.kaydet_not
        )
        self.btn_kaydet.pack(pady=10)

    def kaydet_not(self):
        not_metni = self.txt_not.get("1.0", tk.END).strip()
        if not not_metni:
            messagebox.showwarning("Uyarı", "📭 Lütfen bir not girin!")
            return

        masaustu = os.path.join(os.path.expanduser("~"), "Desktop")
        dosya_yolu = os.path.join(masaustu, "notlar.txt")

        with open(dosya_yolu, "a", encoding="utf-8") as file:
            file.write(not_metni + "\n")

        messagebox.showinfo("Başarılı", "✅ Not başarıyla masaüstüne kaydedildi!")
        self.txt_not.delete("1.0", tk.END)

if __name__ == "__main__":
    app = NotDefteri()
    app.mainloop()
