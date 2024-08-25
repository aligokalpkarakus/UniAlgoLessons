MIN_BILYE = 10
FARKLI_BILYE_SAY_MAX = 1
MIN_AGIRLIK = 0
POZITIFLIK = 0
YUZDE = 100

kutu_sayisi = 0
uretim_hatali_kutu_say = 0
hatasiz_kutu_say = 0
iade_edilen_bilye_say = 0
kabul_edilen_bilye_say = 0
esit_agirlikta_bilye_olan_kutu_say = 0
bir_bilye_agir_olan_kutu = 0
bir_bilye_hafif_olan_kutu = 0
esitte_max_agirlik = 0
esitte_max_bilye_say = 0
max_agirlik_fark = 0
max_yuzde = 0
min_agirlik_fark = 0
min_yuzde = 0
bilye_sayisi_max = 0
agir_fark_top = 0
hafif_fark_top = 0
agirlik_fark_yuzde_top = 0
hafif_fark_yuzde_top = 0
max_agirlik_fark_yuzdesi = 0
isaret = ''
devam = 'E' or 'e'

while devam in ['e', 'E']:
    kutu_sayisi += 1
    farkli_bilye_say = 0

    bilye_sayisi = int(input("Bilye sayısını giriniz (an az 10 adet):"))
    if bilye_sayisi < MIN_BILYE:
        bilye_sayisi = int(input("Lütfen 10 veya 10'dan fazla değer giriniz:"))
    else:
        while bilye_sayisi >= MIN_BILYE:
        bilye_agirlik = int(input("Bilyenin ağırlığını giriniz (mg cinsinden en az 0):"))

        while bilye_agirlik >= MIN_AGIRLIK:

            for bilye_no in range(1, bilye_sayisi):
                bilye_agirlik2 = int(input("Bilyenin ağırlığını giriniz:"))

                if bilye_agirlik != bilye_agirlik2:
                    farkli_bilye_say += 1

                if farkli_bilye_say > FARKLI_BILYE_SAY_MAX:
                    print("Kutu iade edilecek.")
                    uretim_hatali_kutu_say += 1
                    iade_edilen_bilye_say += bilye_sayisi
                    break

                elif farkli_bilye_say == FARKLI_BILYE_SAY_MAX:
                    hatasiz_kutu_say += 1
                    kabul_edilen_bilye_say += bilye_sayisi
                    agirlik_fark = bilye_agirlik - bilye_agirlik2
                    agirlik_fark_yuzde = agirlik_fark * YUZDE / bilye_agirlik2

                    if agirlik_fark > POZITIFLIK:
                        print(f"Farklı bilye daha ağır. Farkları: {agirlik_fark}\nFarklarının yüzdesi: %{agirlik_fark_yuzde:.2f}")
                        bir_bilye_agir_olan_kutu += 1
                        agir_fark_top += agirlik_fark
                        agirlik_fark_yuzde_top += agirlik_fark_yuzde

                    else:
                        bir_bilye_hafif_olan_kutu += 1
                        hafif_fark_top += abs(agirlik_fark)
                        hafif_fark_yuzde_top += abs(agirlik_fark_yuzde)
                        print(f"Farklı bilye daha hafif. Farkları: {agirlik_fark}\nFarklarının yüzdesi: %{agirlik_fark_yuzde:.2f}")

                else:
                    if bilye_agirlik == bilye_agirlik2:
                        esitte_max_agirlik = bilye_agirlik
                        esitte_max_bilye_say = bilye_sayisi
                        esit_agirlikta_bilye_olan_kutu_say += 1
                        hatasiz_kutu_say += 1
                        kabul_edilen_bilye_say += bilye_sayisi
                        print("Bilyeler eşit ağırlıkta.")

                if esitte_max_agirlik < bilye_agirlik:
                    esitte_max_bilye_say = bilye_sayisi
                    esitte_max_agirlik = bilye_agirlik

                if esitte_max_bilye_say < bilye_sayisi:
                    esitte_max_bilye_say = bilye_sayisi
                    esitte_max_agirlik = bilye_agirlik

                if agirlik_fark < POZITIFLIK:
                    max_agirlik_fark = abs(agirlik_fark)
                    isaret = 'hafif'
                else:
                    max_agirlik_fark = agirlik_fark
                    isaret = 'ağır'
                max_agirlik_fark_yuzdesi = max_agirlik_fark * YUZDE / bilye_agirlik2
                max_yuzde = max_agirlik_fark_yuzdesi

                if agirlik_fark_yuzde < max_yuzde:
                    min_agirlik_fark = abs(agirlik_fark)
                    min_yuzde = abs(agirlik_fark_yuzde)
                    if agirlik_fark < POZITIFLIK:
                        isaret = 'hafif'
                    else:
                        isaret = 'ağır'

        devam = input("Devam etmek için e/E, çıkış için h/H harflerini giriniz:")
        if devam in ['h', 'H']:
            break
        else:
            print("Hatalı giriş yaptınız. Tekrar deneyiniz.")

agir_fark_top_ort = agir_fark_top / bir_bilye_agir_olan_kutu
agir_fark_yuzde_top_ort = agirlik_fark_yuzde_top / bir_bilye_agir_olan_kutu
hafif_fark_top_ort = hafif_fark_top / bir_bilye_hafif_olan_kutu
hafif_fark_yuzde_top_ort = hafif_fark_yuzde_top / bir_bilye_hafif_olan_kutu
uretim_hatali_yuzde = uretim_hatali_kutu_say * YUZDE / kutu_sayisi
esit_yuzde = esit_agirlikta_bilye_olan_kutu_say / hatasiz_kutu_say
agir_yuzde = bir_bilye_agir_olan_kutu / hatasiz_kutu_say
hafif_yuzde = bir_bilye_hafif_olan_kutu / hatasiz_kutu_say

print(f"Üretim hatası olan kutu sayısı: {uretim_hatali_kutu_say}\nTüm kutular içindeki yüzdesi: %{uretim_hatali_yuzde:.2f}")
print(f"İade edilen bilye sayısı: {iade_edilen_bilye_say}\nKabul edilen bilye sayısı: {kabul_edilen_bilye_say}")
print(f"Bilyelerin eşit olduğu kutu sayısı: {esit_agirlikta_bilye_olan_kutu_say}\nSatılan kutular içindeki yüzdesi: "
      f"%{esit_yuzde:.2f}")
print(f"Bir bilyenin diğerlerinden daha ağır olduğu kutu sayısı: {bir_bilye_agir_olan_kutu}\nSatılan kutular içindeki "
      f"yüzdesi: %{agir_yuzde}")
print(f"Bir bilyenin diğerlerinden daha hafif olduğu kutu sayısı: {bir_bilye_hafif_olan_kutu}\nSatılan kutular içindeki "
      f"yüzdesi: %{hafif_yuzde}")
print(f"1 bilyenin diğerlerinden daha ağır olduğu kutulardaki ağır olan bilyelerin ağırlık farkı değerlerinin "
      f"ortalamalası: {agir_fark_top_ort:.2f}\nYüzdelerinin ortalaması: {agir_fark_yuzde_top_ort:.2f}")
print(f"1 bilyenin diğerlerinden daha hafif olduğu kutulardaki hafif olan bilyelerin ağırlık farkı değerlerinin "
      f"ortalamalası: {hafif_fark_top_ort:.2f}\nYüzdelerinin ortalaması: {hafif_fark_yuzde_top_ort:.2f}")
print(f"Tüm bilyelerin eşit ağırlıkta olduğu kutular arasında, içinde en çok sayıda bilye olan kutudaki bilye "
      f"sayısı: {esitte_max_bilye_say}\nO kutudaki 1 bilyenin ağırlığı: {esitte_max_agirlik} mg")
print(f"Tüm bilyelerin eşit ağırlıkta olduğu kutular arasında, içinde en ağır bilyeler olan kutudaki bilye "
      f"sayısı: {esitte_max_bilye_say}\nO kutudaki 1 bilyenin ağırlığ: {esitte_max_agirlik} mg")
print(f"Farklı olan bilyenin ağırlığının kutudaki diğer bilyelerin ağırlığıyla arasındaki farkın değerinin en büyük olduğu ağırlık "
      f"farkının değeri: {max_agirlik_fark}\nYüzdesi: %{max_agirlik_fark_yuzdesi}\nİşareti: daha {isaret}")
print(f" Farklı olan bilyenin ağırlığının kutudaki diğer bilyelerin ağırlığıyla arasındaki farkın yüzdesinin "
      f"en küçük olduğu ağırlık farkının değeri: {max_agirlik_fark}\nYüzdesi: %{max_yuzde}\nİşareti: daha {isaret}")