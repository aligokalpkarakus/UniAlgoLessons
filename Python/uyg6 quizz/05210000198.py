def atici_bilgisi(yarismaci_say, ad_soyad):
    # yarışmacıların isim soyisim bilgileri
    for yarismaci_no in range(yarismaci_say):
        yarismaci_ad_soyad = input(f"{yarismaci_no + 1}. yarışmacının adı soyadı:")
        ad_soyad.append(yarismaci_ad_soyad)
        # indeks hatası aldığım için diğer listelerden farklı olarak append kullandım


def istatistikler(yarismaci_say, ad_soyad, puan, on_sayisi, x_sayisi):
    # atış sayısına int değeri girilip girilmediği
    try:
        # yarışmacıların puanlarını hesaplama
        atis_sayisi = int(input("Atış sayısını giriniz:"))
        for atis_no in range(atis_sayisi):
            for yarismaci_no in range(yarismaci_say):
                puan_degeri = int(input(f"{ad_soyad[yarismaci_no]}, {atis_no + 1}. vuruşta kaç sayılık bölgeden vurdu? "
                                        f"(10-9-8-7-6-5). İsabet yoksa 0 giriniz:"))
                puan[yarismaci_no] += puan_degeri

                if puan_degeri == 10:
                    on_sayisi[yarismaci_no] += 1
                    x_kontrol = input(f"{ad_soyad[yarismaci_no]} için X sayısı var mı? e/h:")
                    if x_kontrol == 'e':
                        x_sayisi[yarismaci_no] += 1

        print("Sıra        Ad Soyad        Puan       10 Sayısı         X Sayısı")
        print("----        --------        ----       ---------         --------")

        # yarışmacıları puanlarına göre sıralama
        for sira in range(yarismaci_say):
            yarismaci_no = 0
            for yarismaci_no1 in range(len(puan)):
                for yarismaci_no2 in range(yarismaci_no1 + 1, len(puan)):
                    if puan[yarismaci_no1] == puan[yarismaci_no2]:
                        if on_sayisi[yarismaci_no1] > on_sayisi[yarismaci_no2]:
                            yarismaci_no = yarismaci_no1
                        elif on_sayisi[yarismaci_no1] < on_sayisi[yarismaci_no2]:
                            yarismaci_no = yarismaci_no2
                        else:
                            if x_sayisi[yarismaci_no1] > x_sayisi[yarismaci_no2]:
                                yarismaci_no = yarismaci_no1
                            else:
                                yarismaci_no = yarismaci_no2
                    else:
                        kazanan = max(puan)
                        kazanan_no = puan.index(kazanan)
                        yarismaci_no = kazanan_no

            print(f"{sira+1}", end="           ")
            print(f"{ad_soyad[yarismaci_no]}", end="")
            print(f"{puan[yarismaci_no]:16d}", end="")
            print(f"{on_sayisi[yarismaci_no]:12d}", end="")
            print(f"{x_sayisi[yarismaci_no]:15d}")

            # her karşılaştırmadaki kazananı listeden çıkarmadığımızda her seferinde o kazananın bilgileri yazdırılıyor
            ad_soyad.pop(yarismaci_no)
            puan.pop(yarismaci_no)
            on_sayisi.pop(yarismaci_no)
            x_sayisi.pop(yarismaci_no)
    except ValueError:
        print("Integer değer girilmedi.")


def main():
    # yarışmacı sayısına int değeri girilip girilmediği
    try:
        MIN_YARISMACI_SAY = 8
        yarismaci_say = int(input("Yarışmacı sayısını giriniz (en az 8):"))
        while yarismaci_say < MIN_YARISMACI_SAY:
            yarismaci_say = int(input("Hatalı giriş, lütfen 8 veya 8'den fazla giriniz:"))
        ad_soyad = []
        puan = [0] * yarismaci_say
        on_sayisi = [0] * yarismaci_say
        x_sayisi = [0] * yarismaci_say
        atici_bilgisi(yarismaci_say, ad_soyad)
        istatistikler(yarismaci_say, ad_soyad, puan, on_sayisi, x_sayisi)
    except ValueError:
        print("Integer değer girilmedi.")


main()
