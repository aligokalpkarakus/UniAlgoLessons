gun = int(input("Gün:"))

toplam_yagmur = 0
yagmurlu_gun = 0


for sayac in range(1,gun+1):
    yagmur_miktari = int(input("Yağmur miktarı:"))
    if yagmur_miktari > 0:
        toplam_yagmur += yagmur_miktari
        yagmurlu_gun += 1

yagmurlu_gun_yuzdesi = yagmurlu_gun/gun * 100
gunluk_ortalama_yagis = toplam_yagmur/gun * 100

print(f"Yağmurlu gün sayısı: {yagmurlu_gun}\nYağmurlu gün yüzdesi: %{yagmurlu_gun_yuzdesi}")
print(f"Günlük ortalama yağış miktarı: {gunluk_ortalama_yagis} kg")