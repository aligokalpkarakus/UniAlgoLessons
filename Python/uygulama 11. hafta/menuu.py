def menu_goruntule():
    print("1. Bul...")
    print("2. Tümünü değiştir...")
    print("3. Tek tek değiştir...")
    print("0. Çıkış...")
    print("Seçiminizi giriniz [0-3]: ", end="")


def sayi_al(alt_sinir, ust_sinir):
    """sayi = input("Sayı giriniz:")
    while not (sayi.isdigit() and alt_sinir <= int(sayi) <= ust_sinir):
        sayi = input("Hatalı veri girişi, lütfen tekrar giriniz:")
    return int(sayi)"""

    hatali_giris = True
    while hatali_giris:
        try:
            sayi = int(input("Sayı giriniz: "))
            if alt_sinir <= sayi <= ust_sinir:
                hatali_giris = False
            else:
                print("Hatalı veri girişi, lütfen tekrar giriniz: ", end="")
        except ValueError:
            print("Integer değer girilmedi, lütfen tekrar giriniz: ", end="")
    return sayi


def evet_hayir_al():
    cevap = input("Cevap: ")
    while cevap not in ["e", "E", "h", "H"]:
        cevap = input("Hatalı giriş, lütfen tekrar giriniz: ")
    return cevap


def bul(metin, aranan):
    bulunma_say = 0
    aranan_uzunluk = len(aranan)
    print("No Konum")
    print("-- -----")
    bulunan_konum = metin.find(aranan)
    while bulunan_konum != -1:
        bulunma_say += 1
        print(f"{bulunma_say:2}  {bulunan_konum + 1:3}")
        bulunan_konum = metin.find(aranan, bulunan_konum + aranan_uzunluk)


def tumunu_degistir(metin, eski, yeni):
    return metin.replace(eski, yeni)


def tek_tek_degistir(metin, eski, yeni):
    aranan_uzunluk = len(eski)
    arama_baslangici = 0
    yeni_metin = ""
    bulunan_konum = metin.find(eski, arama_baslangici)
    while bulunan_konum != -1:
        print(f"{bulunan_konum + 1} konumdaki değiştirilsin mi? (e/E/h/H): ", end="")
        degisim = evet_hayir_al()
        yeni_metin = yeni_metin + metin[arama_baslangici:bulunan_konum]
        if degisim.upper() == 'E':
            yeni_metin = yeni_metin + yeni
        else:
            yeni_metin = yeni_metin + eski
        arama_baslangici = bulunan_konum + aranan_uzunluk
        bulunan_konum = metin.find(eski, arama_baslangici)
    yeni_metin = yeni_metin + metin[arama_baslangici:]
    return yeni_metin


def main():
    metin = input("Metninizi giriniz: ")
    cikis = 'H'
    while cikis.upper() == 'H':
        menu_goruntule()
        menu_secim = sayi_al(0, 3)
        if menu_secim == 1:
            aranan = input("Aradığınız metin parçasını giriniz: ")
            bul(metin, aranan)
        elif menu_secim == 2:
            eski = input("Değiştirmek istediğiniz metin parçasını giriniz: ")
            yeni = input("Yerine koymak istediğiniz metin parçasını giriniz: ")
            metin = tumunu_degistir(metin, eski, yeni)
            print(metin)
        elif menu_secim == 3:
            eski = input("Değiştirmek istediğiniz metin parçasını giriniz: ")
            yeni = input("Yerine koymak istediğiniz metin parçasını giriniz: ")
            metin = tek_tek_degistir(metin, eski, yeni)
            print(metin)
        else:
            print("Çıkmak istediğinizden emin misiniz (e/E/h/H) ?: ")
            cikis = evet_hayir_al()


main()
