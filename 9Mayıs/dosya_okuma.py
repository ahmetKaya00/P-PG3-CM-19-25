with open("demo.txt","r",encoding="utf-8") as dosya:
    icerik = dosya.read()
    print(icerik)

with open("demo.txt","w",encoding="utf-8") as dosya:
    dosya.write("Bu bir deneme yazısıdır!\n")
    dosya.write("Bu da bir deneme yazısıdır!\n")

with open("demo.txt","a",encoding="utf-8") as dosya:
    dosya.write("Merhaba!\n")

isim = input("Lütfen adınızı girin:")

with open("deneme.txt","a", encoding="utf-8") as dosya:
    dosya.write(f"Merhaba {isim}!\n Hoş Geldin.")