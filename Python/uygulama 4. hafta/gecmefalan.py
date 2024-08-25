# Sınıftaki öğrenci sayısını ve her öğrencinin arasınav ve final notlarını alan, her öğrencinin dönem sonu notunu ve başarı durumunu (geçme notu 60, arasınav %40 final %60 yazdıran algoritma

ogr_say = int(input("Öğrenci sayısını giriniz : "))

for sayac in range(ogr_say):
    vize_not = int(input("Vize notunuzu giriniz : "))
    final_not = int(input("Final notunuzu giriniz : "))
    donem_sonu = vize_not * 0.4 + final_not * 0.6
    print(donem_sonu)
    if donem_sonu >= 60:
        print("Geçtiniz.")
    else:
        print("Geçemediniz.")
