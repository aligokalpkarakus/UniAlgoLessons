YAS_DONUM = 12
YAVRU_YEM_TL = 50
YETISKIN_YEM_TL = 55
KISIRLASTIRILMIS_YEM_TL = 60


kac_aylik = int(input("Kedinizin kaç aylık olduğunu giriniz:"))
agirlik = float(input("Kedinizin ağırlığını giriniz (kg):"))

if kac_aylik <= YAS_DONUM:
    mama_tipi = "Yavru"
    if 0 < kac_aylik <= 3:
        gunluk_yem_miktari = agirlik * 35 / 1000
    elif 4 <= kac_aylik <= 6:
        gunluk_yem_miktari = agirlik * 3 / 100
    elif 7 <= kac_aylik <= 12:
        gunluk_yem_miktari = agirlik * 25 / 1000

    aylik_masraf = 30 * gunluk_yem_miktari * 50

else:
    kisirlik = input("Kedinizin kısırlaştırılmış olup olmadığını giriniz (e/h):")
    if kisirlik == 'e':
        mama_tipi = "Kısırlaştırılmış"
        gunluk_yem_miktari = agirlik * 15 / 1000
        aylik_masraf = 30 * gunluk_yem_miktari * 60
    else:
        mama_tipi = "Yetişkin"
        gunluk_yem_miktari = agirlik * 15 / 1000
        aylik_masraf = 30 * gunluk_yem_miktari * 55

print("Almanız gereken kedi maması tipi: ",mama_tipi)
print("Kedinize vermeniz gereken günlük mama miktarı: ",gunluk_yem_miktari," gr")
print("Aylık kedi maması masrafınız: ",aylik_masraf," TL")

