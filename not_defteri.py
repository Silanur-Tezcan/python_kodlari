import os

print("📖 Not Defteri - Python")
not_text = input("Kaydetmek istediğiniz notu girin: ")

# Dosyaya not ekleme
with open("notlar.txt", "a") as file:
    file.write(not_text + "\n")

print("✅ Not başarıyla kaydedildi!")