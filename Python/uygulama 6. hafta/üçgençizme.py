# satır sayısı verilen bir ikizkenar üçgen çizdiren fonksiyon

def satir_yazma(uzunluk,karakter):
    for sayac in range(uzunluk+1):
        print(karakter,end="")

satir_sayisi = int(input("Satır sayısı (yükseklik) giriniz: "))

for satir_no in range(1,satir_sayisi +1):
    satir_yazma(satir_sayisi - satir_no, "*")
    satir_yazma(satir_no * 2 - 1, "+")
    satir_yazma(satir_sayisi - satir_no, "/")
    print()