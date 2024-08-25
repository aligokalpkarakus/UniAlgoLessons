#Girilen 2 sayı arasındaki ilişkiyi bulan algoritma:

sayi1 = int(input("Bir sayı giriniz : "))
sayi2 = int(input("Bir sayı giriniz : "))

if sayi1 > sayi2:
    print("Birinci sayı daha büyük.")
elif sayi1 < sayi2:
    print("İkinci sayı daha büyük.")
else:
    print("Sayılar birbirlerine eşit.")
