# Girilen 2 sayının OBEB'ini bulan algoritma

sayi1 = int(input("Bir sayı giriniz : "))
sayi2 = int(input("Bir sayı giriniz : "))

if sayi1 > sayi2:
    bolunen = sayi1
    bolen = sayi2
else:
    bolunen = sayi2
    bolen = sayi1

kalan = bolunen % bolen

while kalan != 0:
    bolunen = bolen
    bolen = kalan
    kalan = bolunen % bolen

print(bolen)
