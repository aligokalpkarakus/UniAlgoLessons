# Girilen 3 farklı sayının ortancasını bulan algoritma:

sayi1 = int(input("Bir sayı giriniz : "))
sayi2 = int(input("Bir sayı giriniz : "))
sayi3 = int(input("Bir sayı giriniz : "))

if sayi1 > sayi2 :
    if sayi1 < sayi3 :
        print("1. sayı ortanca")
    else:
        if sayi2 > sayi3:
            print("2. sayı ortanca")
        else:
            print("3. sayı ortanca")
else:
    if sayi2 < sayi3 :
        print("2. sayı ortanca")
    else:
        print("3. sayı ortanca")