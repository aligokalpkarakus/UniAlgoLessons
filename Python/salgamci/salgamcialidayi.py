BIR_LITRELIK_URETIM = 5
BIR_LITRELIK_SATIS = 7.5
YARIM_LITRELIK_URETIM = 2.5
YARIM_LITRELIK_SATIS = 4
YUZ_ML_URETIM = 0.5
EN_AZ_YARIM_LITRE = 5
EN_AZ_BIR_LITRE = 3
KAGIT_BARDAK = 0.05
YARIM_BARDAK = 0.1
BIR_BARDAK = 0.15

ikram = input("Müşterinin şalgamın tadına bakmak isteyip istemediğini giriniz (e/h) : ")
yarim_litre_sayi = int(input("Müşterinin yarım litrelik şişelerden kaç adet satın almak istediğini (istemiyorsa 0) giriniz : "))
bir_litre_sayi = int(input("Müşterinin bir litrelik şişelerden kaç adet satın almak istediğini (istemiyorsa 0) giriniz : "))

bir_litrelik_maliyet = (BIR_LITRELIK_URETIM + BIR_BARDAK) * bir_litre_sayi
bir_litrelik_kazanc = BIR_LITRELIK_SATIS * bir_litre_sayi
yarim_litrelik_maliyet = (YARIM_LITRELIK_URETIM + YARIM_BARDAK) * yarim_litre_sayi
yarim_litrelik_kazanc = YARIM_LITRELIK_SATIS * yarim_litre_sayi
yuz_ml_maliyet = YUZ_ML_URETIM + KAGIT_BARDAK
askida_maliyet = YARIM_LITRELIK_URETIM + YARIM_BARDAK
musteri_borcu = bir_litrelik_kazanc + yarim_litrelik_kazanc

if bir_litre_sayi > 0 or yarim_litre_sayi > 0:
    musteri_borcu = bir_litrelik_kazanc + yarim_litrelik_kazanc

print(f"Müşterinin ödemesi gereken toplam ücret : {musteri_borcu:.2f} TL.")

toplam_maliyet = bir_litrelik_maliyet + yarim_litrelik_maliyet

if ikram == 'e':
    toplam_maliyet += yuz_ml_maliyet
else:
    toplam_maliyet = bir_litrelik_maliyet + yarim_litrelik_maliyet

if bir_litre_sayi >= EN_AZ_BIR_LITRE or yarim_litre_sayi >= EN_AZ_YARIM_LITRE:
    toplam_maliyet += askida_maliyet
else:
    toplam_maliyet = bir_litrelik_maliyet + yarim_litrelik_maliyet

toplam_kar = musteri_borcu - toplam_maliyet
kar_orani = (musteri_borcu - toplam_maliyet) / toplam_maliyet * 100
musteri_borcu = bir_litrelik_kazanc + yarim_litrelik_kazanc

if toplam_kar > 0:
    print(f"Ali dayı bu müşteriden {toplam_kar:.2f} TL kar etmiştir, kar oranı : % {kar_orani:.2f}")
else:
    print("Ali dayı bu müşteriden zarar etmiştir.")
