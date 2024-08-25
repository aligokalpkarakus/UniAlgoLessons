# SABİTLER
MIN_ADET = 10
MAX_SAYAC = 2
MIN_AGIRLIK = 0
KONTROL_NOKTALARI_1 = 55555
KONTROL_NOKTALARI_2 = 99999
YUZDE = 100
POZITIFLIK = 0

# DEĞİŞKENLER
hatali_kutu_say = 0
uygun_kutu_say = 0
hatali_kutu_bilye_say = 0
uygun_kutu_bilye_say = 0
esit_bilye_olan_kutu_say = 0
bir_agir_olan_kutu_say = 0
bir_hafif_olan_kutu_say = 0
bir_bilyenin_daha_agir_oldugu_fark_top = 0
bir_bilyenin_daha_agir_oldugu_fark_yuzdesi_top = 0
bir_bilyenin_daha_hafif_oldugu_fark_top = 0
bir_bilyenin_daha_hafif_oldugu_fark_yuzdesi_top = 0
esitteki_max_bilye_say = 0
esitteki_max_bilye_olan_kutudaki_bilyenin_agirligi = 0
esitteki_en_agir_kutu_bilye_say = 0
esitteki_en_agir_kutudaki_bilyenin_agirligi = 0
max_fark = 0
max_yuzde = 0
min_yuzde = 9999
min_yuzdenin_agirlik_farki = 9999
isaret = ''
max_isaret = ''
min_isaret = ''
devam = 'e' or 'E'

# DÖNGÜLER
while devam in ['e', 'E']:

    birinci_agirlik = 0
    birinci_agirlik_sayac = 0
    ikinci_agirlik = 0
    ikinci_agirlik_sayac = 0
    kontrol = 0
    genel_agirlik = 0
    farkli_olan_agirlik = 0

    bilye_sayisi = int(input("Bilye sayısını giriniz:"))
    while bilye_sayisi < MIN_ADET:
        bilye_sayisi = int(input("Hatalı giriş. Lütfen 10 veya 10'dan fazla adet belirtin:"))

    for bilye_no in range(1, bilye_sayisi+1):

        bilye_agirligi = int(input(f"{bilye_no}. bilyenin ağırlığını giriniz (mg):"))
        while bilye_agirligi <= MIN_AGIRLIK:
            bilye_agirligi = int(input("Hatalı giriş. Lütfen ağırlığı pozitif değer olarak giriniz:"))

        if bilye_no == 1:
            birinci_agirlik = bilye_agirligi
            birinci_agirlik_sayac += 1

        if bilye_no > 1 and bilye_agirligi == birinci_agirlik:
            birinci_agirlik_sayac += 1

        if bilye_agirligi != birinci_agirlik and ikinci_agirlik == 0:
            # and'in iki kısmının da sağlanıp bu bloğa girmesini istiyorum
            ikinci_agirlik = bilye_agirligi
            ikinci_agirlik_sayac += 1
            kontrol = KONTROL_NOKTALARI_1

        if bilye_agirligi == ikinci_agirlik and kontrol == KONTROL_NOKTALARI_2:
            ikinci_agirlik_sayac += 1

        # bilye no ilerlerken olası durumda ikinci ağırlığı değiştirmek için
        if kontrol == KONTROL_NOKTALARI_1:
            kontrol = KONTROL_NOKTALARI_2

        if (birinci_agirlik_sayac >= MAX_SAYAC and ikinci_agirlik_sayac >= MAX_SAYAC) or \
                (birinci_agirlik != bilye_agirligi and ikinci_agirlik != bilye_agirligi):
            print("Hatalı kutu, iade edilecek.")
            hatali_kutu_say += 1
            hatali_kutu_bilye_say += bilye_sayisi
            break

        if birinci_agirlik_sayac > ikinci_agirlik_sayac:
            genel_agirlik = birinci_agirlik
            farkli_olan_agirlik = ikinci_agirlik
        else:
            genel_agirlik = ikinci_agirlik
            farkli_olan_agirlik = birinci_agirlik

    else:  # kutular hatasızsa devam edilecek blok
        uygun_kutu_say += 1
        uygun_kutu_bilye_say += bilye_sayisi
        if ikinci_agirlik_sayac == 0:  # bilyelerin ağırlıkları eşitse hepsi birinci ağırlığa işleneceği için 0
            esit_bilye_olan_kutu_say += 1
            print("Bu kutudaki bilyeler eşit ağırlıkta.")

            if bilye_sayisi > esitteki_max_bilye_say:
                esitteki_max_bilye_say = bilye_sayisi
                esitteki_max_bilye_olan_kutudaki_bilyenin_agirligi = genel_agirlik

            if birinci_agirlik > esitteki_en_agir_kutudaki_bilyenin_agirligi:
                esitteki_en_agir_kutudaki_bilyenin_agirligi = birinci_agirlik
                esitteki_en_agir_kutu_bilye_say = bilye_sayisi

        else:
            fark = genel_agirlik - farkli_olan_agirlik
            fark_yuzde = abs(fark * YUZDE / genel_agirlik)

            # hafif bilyeye sahip olan kutu
            if fark > POZITIFLIK:
                isaret = 'hafif'
                bir_hafif_olan_kutu_say += 1
                bir_bilyenin_daha_hafif_oldugu_fark_top += fark
                bir_bilyenin_daha_hafif_oldugu_fark_yuzdesi_top += fark_yuzde
                print(f"Farklı olan bilye diğer bilyelerden daha hafiftir. Farkın değeri: {fark}, "
                      f"yüzdesi: %{fark_yuzde:.2f}")

            # ağır bilyeye sahip olan kutu
            else:
                isaret = 'ağır'
                fark = abs(fark)
                bir_agir_olan_kutu_say += 1
                bir_bilyenin_daha_agir_oldugu_fark_top += fark
                bir_bilyenin_daha_agir_oldugu_fark_yuzdesi_top += fark_yuzde
                print(f"Farklı olan bilye diğer bilyelerden daha ağırdır. Farkın değeri: {fark}, "
                      f"yüzdesi: %{fark_yuzde:.2f}")

            if max_fark < fark:
                max_isaret = isaret
                max_fark = fark
                max_yuzde = fark_yuzde

            if min_yuzde > fark_yuzde:
                min_isaret = isaret
                min_yuzde = fark_yuzde
                min_yuzdenin_agirlik_farki = fark

    devam = input("Devam etmek için e/E, çıkış için h/H giriniz:")
    while devam not in ['e', 'E', 'h', 'H']:
        devam = input("Hatalı giriş. Lütfen devam etmek için e/E, çıkış için h/H giriniz:")
    if devam in ['h', 'H']:
        print("Girilecek kutu bilgisi kalmadı..")
    else:
        print("Yeni kutu girişi...")

# İŞLEMLER
toplam_kutu = hatali_kutu_say + uygun_kutu_say
hatali_tum_kutulardaki_yuzdesi = hatali_kutu_say * YUZDE / toplam_kutu
hatasiz_kutu_say = toplam_kutu - hatali_kutu_say
esit_bilye_olan_kutu_say_yuzde = esit_bilye_olan_kutu_say * YUZDE / hatasiz_kutu_say
bir_agir_olan_kutu_say_yuzde = bir_agir_olan_kutu_say * YUZDE / hatasiz_kutu_say
bir_hafif_olan_kutu_say_yuzde = bir_hafif_olan_kutu_say * YUZDE / hatasiz_kutu_say
bir_bilyenin_daha_agir_oldugu_fark_top_ort = bir_bilyenin_daha_agir_oldugu_fark_top / bir_agir_olan_kutu_say
bir_bilyenin_daha_agir_oldugu_fark_yuzdesi_top_ort = bir_bilyenin_daha_agir_oldugu_fark_yuzdesi_top / \
                                                     bir_agir_olan_kutu_say
bir_bilyenin_daha_hafif_oldugu_fark_top_ort = bir_bilyenin_daha_hafif_oldugu_fark_top / bir_hafif_olan_kutu_say
bir_bilyenin_daha_hafif_oldugu_fark_yuzdesi_top_ort = bir_bilyenin_daha_hafif_oldugu_fark_yuzdesi_top / \
                                                      bir_hafif_olan_kutu_say
# ÇIKTILAR
print(f"Üretim hatası olan kutu sayısı: {hatali_kutu_say}, "
      f"tüm kutulardaki yüzdesi: %{hatali_tum_kutulardaki_yuzdesi:.2f}")
print(f"İade edilen bilye sayısı: {hatali_kutu_bilye_say}, kabul edilen bilye sayısı: {uygun_kutu_bilye_say}")
print(f"Tüm bilyelerin eşit olduğu kutu sayısı: {esit_bilye_olan_kutu_say}, hata olmayan kutular içindeki yüzdesi:"
      f" %{esit_bilye_olan_kutu_say_yuzde:.2f} ")
print(f"1 bilyenin diğerlerinden daha ağır olduğu kutu sayısı: {bir_agir_olan_kutu_say},"
      f" hata olmayan kutular içindeki yüzdesi: %{bir_agir_olan_kutu_say_yuzde:.2f}")
print(f"1 bilyenin diğerlerinden daha hafif olduğu kutu sayısı: {bir_hafif_olan_kutu_say},"
      f" hata olmayan kutular içindeki yüzdesi: %{bir_hafif_olan_kutu_say_yuzde:.2f}")
print(f"1 bilyenin diğerlerinden daha ağır olduğu kutulardaki ağır olan bilyelerin "
      f"ağırlık farkı değerlerinin ortalaması: {bir_bilyenin_daha_agir_oldugu_fark_top_ort:.2f}")
print(f"1 bilyenin diğerlerinden daha ağır olduğu kutulardaki ağır olan bilyelerin "
      f"ağırlık farkı yüzdelerinin ortalaması: %{bir_bilyenin_daha_agir_oldugu_fark_yuzdesi_top_ort:.2f}")
print(f"1 bilyenin diğerlerinden daha hafif olduğu kutulardaki hafif olan bilyelerin "
      f"ağırlık farkı değerlerinin ortalaması: {bir_bilyenin_daha_hafif_oldugu_fark_top_ort:.2f}")
print(f"1 bilyenin diğerlerinden daha hafif olduğu kutulardaki hafif olan bilyelerin "
      f"ağırlık farkı yüzdelerinin ortalaması: %{bir_bilyenin_daha_hafif_oldugu_fark_yuzdesi_top_ort:.2f}")
print(f"Tüm bilyelerin eşit ağırlıkta olduğu kutular arasında, "
      f"içinde en çok sayıda bilye olan kutudaki bilye sayısı: {esitteki_max_bilye_say}"
      f"\nO kutudaki 1 bilyenin ağırlığı: {esitteki_max_bilye_olan_kutudaki_bilyenin_agirligi} mg")
print(f"Tüm bilyelerin eşit ağırlıkta olduğu kutular arasında, "
      f"içinde en ağır bilyeler olan kutudaki bilye sayısı: {esitteki_en_agir_kutu_bilye_say}"
      f"\nO kutudaki 1 bilyenin ağırlığo: {esitteki_en_agir_kutudaki_bilyenin_agirligi} mg")
print(f"Farklı olan bilyenin ağırlığının kutudaki diğer bilyelerin ağırlığıyla "
      f"arasındaki farkın değerinin en büyük olduğu ağırlık farkının değeri: {max_fark}\n"
      f"Yüzdesi: %{max_yuzde:.2f}\nİşareti (ağır ya da hafif): {max_isaret}")
print(f"Farklı olan bilyenin ağırlığının kutudaki diğer bilyelerin ağırlığıyla "
      f"arasındaki farkın yüzdesinin en küçük olduğu ağırlık farkının değeri: {min_yuzdenin_agirlik_farki}"
      f"\nYüzdesi: %{min_yuzde:.2f}\nİşareti (ağır ya da hafif): {min_isaret}")
