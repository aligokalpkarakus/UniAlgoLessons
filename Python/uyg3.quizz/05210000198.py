# Sabit
NORMAL_SEZON_MAC_SAYISI = 26

# Girdiler
yas = int(input("Yaşınızı giriniz : "))
son_yillik_ucret = int(input("Son yıllık ücretinizi giriniz (TL) : "))
takim_sirasi = int(input("Takımınızın normal sezon sonundaki sırasını giriniz : "))

if takim_sirasi > 8:
    mac_basina_maliyet = son_yillik_ucret / NORMAL_SEZON_MAC_SAYISI
else:
    playoff_mac_sayisi = int(input("Takımınızın playoff sezonunda oynadığı maç sayısını giriniz : "))
    mac_basina_maliyet = son_yillik_ucret / (NORMAL_SEZON_MAC_SAYISI + playoff_mac_sayisi)

# Durumlar
if yas < 22:
    serbest_kalma_ucreti = 'Serbest kalma (takımınızdan ayrılma) hakkınız bulunmamaktadır.'
elif yas == 22:
    serbest_kalma_ucreti = son_yillik_ucret * 2
elif yas == 23:
    serbest_kalma_ucreti = son_yillik_ucret * 2
elif yas == 24:
    serbest_kalma_ucreti = son_yillik_ucret / 2
else:
    serbest_kalma_ucreti = 0.00

# Çıktılar
print(f"Oynadığınız maç başına takımınıza maliyetiniz : {mac_basina_maliyet:.2f} TL")

if yas < 22:
    print(serbest_kalma_ucreti)
else:
    print(f"Serbest kalma (takımınızdan ayrılma) hakkınız bulunmaktadır, serbest kalma bedeliniz : {serbest_kalma_ucreti:.2f} TL")