# Girilen 3 farklı sayının en büyüğünü bulan algoritma:

sayi1 = int(input("Bir sayı giriniz : "))
sayi2 = int(input("Bir sayı giriniz : "))
sayi3 = int(input("Bir sayı giriniz : "))

if sayi1 > sayi2 :
    if sayi1 > sayi3 :
        print("Birinci sayı en büyüktür.")
    else:
        print("Üçüncü sayı en büyüktür")

else:
    if sayi2 > sayi3 :
        print("İkinci sayı en büyüktür.")
    else:
        print("Üçüncü sayı en büyüktür.")