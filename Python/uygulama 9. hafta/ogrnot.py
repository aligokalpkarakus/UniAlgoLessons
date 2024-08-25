# Önce bir sınıftaki öğrenci sayısını daha sonra öğrencilerin notlarını kullanıcıdan alan ve sınıf ortalamasının
# üstünde olan öğrenci notlarını listeleyen algoritma.

ogr_say = int(input("Öğrenci sayısını giriniz:"))
not_top = 0
notlar = [0] * ogr_say # öğrenci sayısı kadar bellekte yer açılacak değerler girilecek.

for ogr_sira_no in range(ogr_say):
    notlar[ogr_sira_no] = int(input("Öğrenci notu:"))
    not_top += notlar[ogr_sira_no]  # burayı sum(notlar[ogr_sira_no] şeklinde de yapabiliriz

ort = not_top / ogr_say

for ogr_sira_no in range(ogr_say):
    if notlar[ogr_sira_no] > ort:
        print(notlar[ogr_sira_no])