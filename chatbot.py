def chatbot():
    print("Chatbot: Merhaba! Size nasıl yardımcı olabilirim? (Çıkış yapmak için 'çıkış' yazın)")

    while True:
        user_input = input("Sen: ").lower()

        # Önceden tanımlanmış yanıtlar
        responses = {
            "merhaba": "Merhaba! Nasılsınız?",
            "nasılsın": "Ben bir yapay zeka olduğum için duygularım yok ama size yardımcı olabilirim!",
            "hava nasıl": "Hava durumunu öğrenmek için bir hava durumu API'si kullanabilirsiniz.",
            "görüşürüz": "Görüşmek üzere! İyi günler."
        }

        # Kullanıcının mesajı listede varsa cevap ver
        if user_input in responses:
            print("Chatbot:", responses[user_input])

        elif user_input == "çıkış":
            print("Chatbot: Görüşmek üzere! Çıkış yapılıyor...")
            break

        else:
            print("Chatbot: Üzgünüm, sizi anlayamadım.")

# Chatbot'u başlat
chatbot()