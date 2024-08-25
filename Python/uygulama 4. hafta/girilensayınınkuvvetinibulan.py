# Girilen bir sayının girilen bir kuvvettinin çıktısını veren

sayi = int(input("Bir sayı giriniz : "))
us = int(input("Üssünü giriniz : "))
carpim = 1

for sayac in range(us):
    carpim = carpim*sayi
    print(carpim)