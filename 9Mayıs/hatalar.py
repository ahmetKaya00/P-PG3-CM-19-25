try:
    sayi = int(input("Bir Sayi Giriniz:"))
    sanuc = 10 / sayi
except ZeroDivisionError:
    print("Sıfıra Bölünmez!")
except ValueError:
    print("Lütfen Geçerli Bir Sayı Girin!")

try:
    demo = open("demo.txt","r",encoding="utf-8")
except:
    print("Bir hata oluştu!")
finally:
    print(demo.close())

yas = int(input("Yaşınızı Girin: "))
if yas < 0:
    raise ValueError("Yaş Negatif Olamaz!")