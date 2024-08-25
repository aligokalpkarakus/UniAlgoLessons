KAZA_NEDENI_SAY = 10


def kaza_verilerini_al_ve_listeleri_olustur(kaza_dosyasi, tum_kaza_sayilari, tum_hasar_tutarlari):
    il_kodu_str = kaza_dosyasi.readline()
    while il_kodu_str != "":
        il_kodu = int(il_kodu_str)
        kaza_nedeni_kodu = int(kaza_dosyasi.readline())
        hasar_tutari = int(kaza_dosyasi.readline())
        # verileri, kaza sayilari ve hasar tutarlari listelerine isle
        tum_kaza_sayilari[il_kodu-1][kaza_nedeni_kodu-1] += 1
        tum_hasar_tutarlari[il_kodu-1][kaza_nedeni_kodu-1] += hasar_tutari
        il_kodu_str = kaza_dosyasi.readline()


def tablo_yazdir(iki_boyutlu_liste):
    kaza_nedenleri = ["Aşırı Hız", "Kural İhlali", "Dikkatsizlik", "Sollama", "Uykusuzluk",
                      "Acemilik", "Alkol", "Yakın Takip", "Agresiflik", "Diğer"]
    print("İl Kodu ",end="")
    for kaza_nedeni in kaza_nedenleri:
        print(f"{kaza_nedeni:13}",end="")
    print("Toplam")
    print("------- ",end="")
    for k in range(KAZA_NEDENI_SAY):
        print("------------ ",end="")
    print("------")
    sutun_toplam = [0] * 10
    for i in range(len(iki_boyutlu_liste)):
        print(i+1,end="")
        counter = 0
        for bilgi in iki_boyutlu_liste[i]:
            print(f"{bilgi:13}", end="")
            sutun_toplam[counter] += bilgi
            counter += 1
        print(f"{sum(iki_boyutlu_liste[i]):13}")
    # tabloyu, tablonun satir ve sutun toplamlarini yazdir
    print("Toplam",end="")
    for bilgi in sutun_toplam:
        print(f"{bilgi:12}",end="")
    print(f"{sum(sutun_toplam):13}")

def main():
    try:
        kaza_dosyasi=open("kazalar.txt","r")
        # illere ve kaza nedenlerine gore yillik kaza sayilari ve yillik hasar tutarlari icin 2 adet iki boyutlu liste yarat
        tum_kaza_sayilari = []
        tum_hasar_tutarlari = []
        for i in range(81):
            bir_il_kaza_sayilari = [0] * KAZA_NEDENI_SAY
            tum_kaza_sayilari.append(bir_il_kaza_sayilari)
            bir_il_hasar_tutarlari = [0] * 10
            tum_hasar_tutarlari.append(bir_il_hasar_tutarlari)
        # kaza verilerini dosyadan almak ve listeleri olusturmak icin ilgili fonksiyonu cagir

        kaza_verilerini_al_ve_listeleri_olustur(kaza_dosyasi, tum_kaza_sayilari, tum_hasar_tutarlari)
        kaza_dosyasi.close()
    except IOError:
        print("Veri dosyası açılamadı ya da okunamadı!")
    else:
        print("İllere ve Kaza Nedenlerine Göre Yıllık Kaza Sayıları")
        # yillik kaza sayilari tablosunu yazdirmak icin ilgili fonksiyonu cagir
        tablo_yazdir(tum_kaza_sayilari)
        bir_tus=input("devam etmek için bir tuşa ve enter'a basınız...")
        print("İllere ve Kaza Nedenlerine Göre Yıllık Hasar Tutarları")
        # yillik hasar tutarlari tablosunu yazdirmak icin ilgili fonksiyonu cagir
        tablo_yazdir(tum_hasar_tutarlari)

main()
