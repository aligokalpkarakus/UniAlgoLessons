# Bir dersi alan öğrencilerin notlarını alan (veri sonu için -1) ve derse ilişkin sınıf not ortalamasının başarılı öğrenci sayısını ( geçme not 60 ) ve başarı yüzdesini bulan algoritma

ogr_not = int(input("Notunuzu giriniz : "))
ogr_say = 0
toplam_not = 0
basarili_sayisi = 0

while ogr_not != -1:
    if ogr_not >= 60:
        basarili_sayisi += 1
    ogr_say += 1
    toplam_not += ogr_not

    ogr_not = int(input("Notunuzu giriniz : "))
print(toplam_not/ogr_say)
print(basarili_sayisi * 100 / ogr_say)
