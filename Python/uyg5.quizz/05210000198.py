# sabitler
MAX_SET = 5
KAZANMA_SETI = 3

# veri girişi
toplam_mac = int(input("Yapılan maç sayısını giriniz: "))

# değişkenler
mac_kazanma = 0
mac_kaybetme = 0
max_fark = 0
sezonluk_kazanilan = 0
sezonluk_kaybedilen = 0
set_kayipsiz = 0
bes_setli_mac = 0

# döngü
for mac_no in range(toplam_mac):
    rakip = input("Rakip takımın ismini giriniz: ")
    kazanilan_sayi_top = 0
    kaybedilen_sayi_top = 0
    kazanilan_set = 0
    kaybedilen_set = 0
    guncel_fark = 0
    for set_no in range(1, MAX_SET+1):
        kazanilan_sayi = int(input("Kazanılan sayıyı giriniz: "))
        kaybedilen_sayi = int(input("Kaybedilen sayıyı giriniz: "))
        kazanilan_sayi_top += kazanilan_sayi
        kaybedilen_sayi_top += kaybedilen_sayi

        if kazanilan_sayi > kaybedilen_sayi:
            kazanilan_set += 1
        else:
            kaybedilen_set += 1

        if kazanilan_set == KAZANMA_SETI or kaybedilen_set == KAZANMA_SETI:
            break

    toplam_set = kazanilan_set + kaybedilen_set
    set_basina_kazanilan_sayi_ort = kazanilan_sayi_top / toplam_set
    set_basina_kaybedilen_sayi_ort = kaybedilen_sayi_top / toplam_set

    print(f"Kazanılan toplam sayı adedi: {kazanilan_sayi_top}")
    print(f"Kaybedilen toplam sayı adedi: {kaybedilen_sayi_top}")
    print(f"Kazanılan toplam set adedi: {kazanilan_set}")
    print(f"Kaybedilen toplam set adedi: {kaybedilen_set}")
    print(f"Set başına kazanılan sayı ortalaması: {set_basina_kazanilan_sayi_ort:.2f}/"
          f"Set başına kaybedilen sayı ortalaması: {set_basina_kaybedilen_sayi_ort:.2f}")

    guncel_fark = kazanilan_sayi_top - kaybedilen_sayi_top
    if guncel_fark < 0:
        guncel_fark *= -1

    if guncel_fark > max_fark:
        max_fark = guncel_fark
        rakip_takim = rakip

    if -1 <= kazanilan_set - kaybedilen_set <= 1:
        bes_setli_mac += 1

    if kazanilan_set == 3 and kaybedilen_set == 0:
        set_kayipsiz += 1

    if kazanilan_set > kaybedilen_set:
        mac_kazanma += 1
    else:
        mac_kaybetme += 1

    sezonluk_kazanilan += kazanilan_sayi_top
    sezonluk_kaybedilen += kaybedilen_sayi_top

mac_basina_kazanilan_sayi_ort = sezonluk_kazanilan / toplam_mac
set_kayipsiz_oran = set_kayipsiz * 100 / mac_kazanma
bes_setli_mac_oran = bes_setli_mac * 100 / toplam_mac

# çıktılar
print(f"Kazanılan toplam sayı adedi: {sezonluk_kazanilan},/"
      f" maç başına kazanılan sayı ortalaması: %{mac_basina_kazanilan_sayi_ort:.2f}")
print(f"Kazanılan maç adedi: {mac_kazanma}, kaybedilen maç adedi: {mac_kaybetme}")
print(f"Set kaybetmeden kazandığı maçların adedi: {set_kayipsiz},/"
      f" tüm kazanılan maçlar içindeki oranı: %{set_kayipsiz_oran:.2f}")
print(f"5 sette biten maçların sayısı: {bes_setli_mac} ve tüm maçlar içindeki oranı: %{bes_setli_mac_oran:.2f}")
print(f"Kazandığı toplam sayı ile kaybettiği toplam sayı arasındaki farkın en yüksek olduğu maçtaki kazandığı /"
      f"toplam sayı ile kaybettiği toplam sayı arasındaki fark: {max_fark}, rakip takımın adı: {rakip_takim}")
