# sabitler
DUSUK_SINIR = 10000
ORTA_SINIR = 25000
DUSUK_GELIR_VERGI = 0.15
ORTA_GELIR_VERGI = 0.2
YUKSEK_GELIR_VERGI = 0.25

brut_maas = int(input("Satış temsilcinizin alacağı brüt maaşı giriniz (TL):"))

# toplarken kullanılacaklar
brut_dusuk_kisi_top = 0
brut_orta_kisi_top = 0
brut_yuksek_kisi_top = 0
net_maas_top = 0
gelir_vergisi_top = 0
brut_top = 0
brut_buyuk_50000 = 0

# döngü
while not brut_maas <= 0:
    if brut_maas <= DUSUK_SINIR:
        gelir_vergisi = brut_maas * DUSUK_GELIR_VERGI
        net_maas = brut_maas - gelir_vergisi
        brut_dusuk_kisi_top += 1
    elif DUSUK_SINIR < brut_maas < ORTA_SINIR:
        gelir_vergisi = brut_maas * ORTA_GELIR_VERGI
        net_maas = brut_maas - gelir_vergisi
        brut_orta_kisi_top += 1
    else:
        gelir_vergisi = brut_maas * YUKSEK_GELIR_VERGI
        net_maas = brut_maas - gelir_vergisi
        brut_yuksek_kisi_top += 1
        if brut_maas >= 50000:
            brut_buyuk_50000 += 1

    gelir_vergisi_top += gelir_vergisi
    brut_top += brut_maas
    net_maas_top += net_maas

    print(f"Devlete ödenecek gelir vergisi tutarı : {gelir_vergisi:.2f} TL")
    print(f"Satış temsilcisine ödenecek net maaş tutarı : {net_maas:.2f} TL")

    brut_maas = int(input("Satış temsilcinizin alacağı brüt maaşı giriniz (TL) (Çıkış için 0 veya negatif bir tam sayı giriniz) :"))

# işlemler
temsilci_sayi_top = brut_dusuk_kisi_top + brut_orta_kisi_top + brut_yuksek_kisi_top
yuksek_50000_oran = brut_buyuk_50000 / brut_yuksek_kisi_top * 100
vergi_brut_oran = gelir_vergisi_top / brut_top * 100
net_maas_ortalamasi = net_maas_top / temsilci_sayi_top

# çıktılar
print(f"Düşük brüt maaşlı temsilci sayısı : {brut_dusuk_kisi_top}\nOrta brüt maaşlı temsilci sayısı : {brut_orta_kisi_top}\nYüksek brüt maaşlı temsilci sayısı : {brut_yuksek_kisi_top}")
print(f"Brüt maaş tutarı 50000 TL’den çok olan satış temsilcilerinin, brüt maaş seviyesi yüksek olan satış temsilcileri içindeki yüzdesi: %{yuksek_50000_oran:.2f}")
print(f"Tüm satış temsilcilerinin net maaş tutarı ortalaması : {net_maas_ortalamasi:.2f} TL")
print(f"Devlete ödenecek toplam gelir vergisi tutarı : {gelir_vergisi_top:.2f} TL\nBu tutarın toplam brüt maaşı tutarı içindeki yüzdesi : %{vergi_brut_oran:.2f}")
