def okcu_bilgi(okcu_sayisi, okcu, bir_okcunun_top_puani, ruzgarlar, puanlar):
    ISABETSIZ = 0
    global isabetli, iska  # değişkenleri farklı fonksiyonlarda da kullanabilmek için
    iska = 0
    isabetli = 0
    atis_hakki = int(input("Atış hakkını giriniz:"))
    for atis_no in range(atis_hakki):
        for okcu_no in range(okcu_sayisi):
            kazanilan_puan = int(input(f"{okcu_no + 1}. okçunun {atis_no + 1}. atıştan kazandığı puan [0-10]:"))
            while not 0 <= kazanilan_puan <= 10:  # puanlar sözlüğünün doğru çalışması için yaptım
                kazanilan_puan = int(input(f"{okcu_no+1}. okçunun {atis_no+1}. atışını [0-10] değerlerince giriniz:"))
            bir_okcunun_top_puani[okcu_no] += kazanilan_puan
            if kazanilan_puan == ISABETSIZ:
                iska += 1
                puanlar[kazanilan_puan] += 1
                okcu[okcu_no][10-kazanilan_puan] += 1
                ruzgar_adi = input("Rüzgar adını giriniz:")
                if ruzgar_adi in ruzgarlar:  # rüzgarlar sözlüğünün kullanılabilmesi için
                    ruzgarlar[ruzgar_adi] += 1
                else:
                    ruzgar_adi = input("Hatalı giriş. Rüzgar adını tekrar giriniz:")
            else:
                isabetli += 1
                puanlar[kazanilan_puan] += 1
                okcu[okcu_no][10-kazanilan_puan] += 1


def tablo_okcu(okcu, bir_okcunun_top_puani, puanlar):  # okçuların puan tablosu
    global isabetli, iska  # değişkeni farklı fonksiyondan almak için
    if isabetli != 0:
        print("Okçu Kayıt No", end="")
        for puan in range(10, -1, -1):
            print(f"{puan:8}P", end="")
        print("     Toplam Puan")
        print("-------------     ", end="")
        for cizgi in range(len(puanlar)):
            print("-----    ", end="")
        print("-----------")
        for okcu_no in range(len(okcu)):
            print(f"{okcu_no + 1}           ", end="")
            for adet in okcu[okcu_no]:
                print(f"{adet:9}", end="")
            print(f"  {bir_okcunun_top_puani[okcu_no]:10}")
        print("Tüm Okçular(%)", end="")
        for i in puanlar:
            print(f"{puanlar[i]*100 / (isabetli+iska):9.2f}", end="")
    else:
        print("İsabetli atış yok.")


def tablo_ruzgar(ruzgarlar):  # ıska atışlar için rüzgarların tablosu
    global iska  # değişkeni farklı fonksiyondan almak için
    print("")  # çıktıda printler çakışıyordu boşluk printleyerek çözdüm
    if iska != 0:  # ıska sayısı 0 ise division by zero hatasından kurtulmak için try except yerine yaptım.
        print("Rüzgar Adı  ", end="")
        print(" Iska Atış Oranı (%)",)
        print("----------  ", end="")
        print(" -------------------")
        for ruzgar_adi in ruzgarlar:
            print(f"{ruzgar_adi}", end="")
            print(f"{ruzgarlar[ruzgar_adi] * 100 / iska:15.2f}")
    else:
        print("Tüm atışlar isabetli.")


def main():
    try:
        okcu_sayisi = int(input("Okçu sayısını giriniz:"))
        while okcu_sayisi < 10:  # okçu sayısının kontrolü
            okcu_sayisi = int(input("Okçu sayısı en az 10 olmalı. Tekrar giriniz:"))
        okcu = []
        bir_okcunun_top_puani = [0] * okcu_sayisi
        puanlar = {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0}
        ruzgarlar = {"Yıldız": 0, "Poyraz": 0, "Gündoğusu": 0, "Keşişleme": 0, "Kıble": 0, "Lodos": 0, "Günbatısı": 0,
                     "Karayel": 0}
        for i in range(okcu_sayisi):
            okcu_puan = [0] * len(puanlar)
            okcu.append(okcu_puan)
        okcu_bilgi(okcu_sayisi, okcu, bir_okcunun_top_puani, ruzgarlar, puanlar)
        tablo_okcu(okcu, bir_okcunun_top_puani, puanlar)
        tablo_ruzgar(ruzgarlar)
    except ValueError:
        print("Integer değer girilmedi.")


main()
