from random import randint

MAX_SAYI = 100
MIN_SAYI = 1

sayi = randint(MIN_SAYI, MAX_SAYI)
tahmin = -1
# tahmin 0 da olabilir , 1 ve 100 arasında olmadığı sürece sıkıntı yok
tahmin_sayac = 0

while sayi != tahmin:
    tahmin = int(input("Tahmininiz:"))
    if sayi < tahmin:
        print("AŞAĞI")
    elif tahmin < sayi:
        print("YUKARI")

    tahmin_sayac += 1

print(f"TEBRİKLER!\nTahmin Sayısı: {tahmin_sayac} ")
