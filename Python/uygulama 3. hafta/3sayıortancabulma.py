# Girilen 3 farklı sayının ortancasını bulan algoritma:

sayi1 = int(input("Bir sayı giriniz : "))
sayi2 = int(input("Bir sayı giriniz : "))
sayi3 = int(input("Bir sayı giriniz : "))

if sayi1 > sayi2 and sayi1 < sayi3 or sayi1 > sayi3 and sayi1 < sayi2:
    print("Birinci sayı ortanca.")

else:
    if sayi2 > sayi1 and sayi2 < sayi3 or sayi2 > sayi3 and sayi2 < sayi1:
        print("İkinci sayı ortanca.")
    else:
        print("Üçüncü sayı ortanca.")