import sys
import random
import string
import tkinter as tk

# Şifre oluşturma fonksiyonu
def generate_password():
    password_length = int(entry_length.get())  # Kullanıcının girdiği uzunluk
    characters = string.ascii_letters + string.digits + string.punctuation  # Kullanılacak karakterler
    password = ''.join(random.choice(characters) for i in range(password_length))  # Şifre oluşturuluyor
    label_result.config(text="Oluşturulan Şifre: " + password)  # Sonuç etiketini güncelliyoruz

# Uygulama penceresini oluştur
root = tk.Tk()
root.title("Güçlü Şifre Oluşturucu")
root.geometry("500x400")  # Pencere boyutunu büyütüyoruz
root.config(bg="#f0f0f0")  # Arka plan rengini değiştiriyoruz

# Şifre uzunluğu giriş alanı
label_length = tk.Label(root, text="Şifre Uzunluğunu Girin:", font=("Helvetica", 12), bg="#f0f0f0")
label_length.pack(pady=20)  # padding ile boşluk ekliyoruz

entry_length = tk.Entry(root, font=("Helvetica", 14), width=15, justify="center")
entry_length.pack(pady=10)

# Şifre oluşturma butonu
button_generate = tk.Button(root, text="Şifreyi Oluştur", command=generate_password, font=("Helvetica", 12), bg="#4CAF50", fg="white", relief="raised", bd=4)
button_generate.pack(pady=20)

# Sonuç etiketi
label_result = tk.Label(root, text="Oluşturulan Şifre: ", font=("Helvetica", 14), bg="#f0f0f0", fg="#333")
label_result.pack(pady=20)

# Pencereyi başlat
root.mainloop()
