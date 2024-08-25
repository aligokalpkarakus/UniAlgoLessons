# Problem:
# Bir dersi alan öğrencilerin notlarını (100’lük sistemde) kullanıcıdan alan (her öğrenciden sonra
# başka öğrenci olup olmadığını soran) ve sınıfla ilgili aşağıda belirtilen istatistiksel bilgileri
# listeleyen bir algoritma ve program yazınız (hatalı veri girişi yapılmayacağını varsayınız):
# - Sınıf not ortalaması
# - Standart sapma
# - Notu, sınıf not ortalamasının üstünde olan öğrencilerin sayısı ve sınıf içindeki yüzdesi
# - Sınıftaki en yüksek ve en düşük notlar


#Algoritma:
#def notlari_al(notlar):
#    devam = 'e'
#    while devam in ['e', 'E']:
#        bir_not=input()
#        notlar.append(bir_not)
#        devam = input()
#
#def istatistikler(notlar):
#    ogr_say = len(notlar)
#    sinif_ort = sum(notlar) / ogr_say
#
#    fark_kare_top = 0
#    ort_ustu_say = 0
#
#    for i in range(ogr_say):
#        fark_kare_top+=(notlar[i] - sinif_ort)**2
#        if notlar[i]>sinif_ort:
#            ort_ustu_say+=1
#
#    print(sinif_ort)
#    std_sapma = (fark_kare_top / (ogr_say - 1))**0.5
#    print(std_sapma)
#    print(ort_ustu_say, ort_ustu_say * 100 / ogr_say)
#    print(max(notlar))
#    print(min(notlar))
#
#def main():
#    notlar = []
#    notlari_al(notlar)
#    istatistikler(notlar)
#
#main()


#Program:
def notlari_al(notlar):
    devam = 'e'
    while devam in ['e', 'E']:
        bir_not=int(input("Siradaki ogrencinin notunu giriniz:"))
        # girilen notlar, listenin sonuna ekleniyor
        notlar.append(bir_not)
        devam = input("baska ogrenci var mi?(eEhH):")

def istatistikler(notlar):
    ogr_say = len(notlar)
    sinif_ort = sum(notlar) / ogr_say
    # sum fonksiyonu, elemanlari sayisal degerler olan bir listenin
    # tum elemanlarinin toplamini bulur ve geri dondurur

    fark_kare_top = 0
    ort_ustu_say = 0

    # for i in range(ogr_say):
    #     fark_kare_top+=(notlar[i] - sinif_ort)**2
    #     if notlar[i]>sinif_ort:
    #         ort_ustu_say+=1
    for bir_not in notlar:  # Yukaridaki kodla ayni isi yapar
        fark_kare_top += (bir_not - sinif_ort)**2
        if bir_not > sinif_ort:
            ort_ustu_say += 1

    print(f"Sinifin not ortalamasi: {sinif_ort:.2f}")
    try:
        std_sapma = (fark_kare_top / (ogr_say - 1))**0.5
    except ZeroDivisionError:
        print("Tek ogrenci icin standart sapma hesaplanamaz!")
    else:  # Istisna olusmazsa...
        print(f"Standart sapma: {std_sapma:.2f}")
    print(f"Sinif not ortalamasinin ustundeki ogrencilerin sayisi: {ort_ustu_say} ve yuzdesi: %{ort_ustu_say*100/ogr_say:.2f}")
    print(f"Siniftaki en yuksek not: {max(notlar)}")
    print(f"Siniftaki en dusuk not: {min(notlar)}")

def main():
    notlar = []  # ogr notlarını saklamak icin bos bir liste yaratiliyor
    notlari_al(notlar)
    # listeler "mutable" oldugu icin, notlari_al fonksiyonunda
    # notlar listesinde yapilan degisiklikler burada da gecerli
    istatistikler(notlar)

main()
