urun_adi = input("Urun adı giriniz = ")
onceki_fiyati = float(input("Onceki fiyatı giriniz = "))
simdiki_fiyati = float(input("Simdiki fiyatı giriniz = "))
fiyat_farki = simdiki_fiyati - onceki_fiyati
fiyat_degisim_orani = fiyat_farki * 100 / onceki_fiyati

print(f"{urun_adi} ürünün fiyatındaki aylık değişim ; ")
print(f"miktarı {fiyat_farki : .2f} TL")
print(f"fiyat değişim oranı {fiyat_degisim_orani}")
