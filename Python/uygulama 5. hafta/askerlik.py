BOY = 175
KILO = 75

max_boy = 174
min_kilo = 76
devam = input("Devam etmek istiyor musunuz e/h:")

while devam == "e" or devam == "E":
    ad = input("Adınız:")
    soyad = input("Soyad:")
    boy = float(input("Boyunuz:"))
    kilo = float(input("Kilonuz:"))
    if boy > 175 and kilo < 75:
        print("Kazandınız!")
        if boy > max_boy:
            max_boy = boy
            max_boy_ad = ad
            max_boy_soyad = soyad
        if kilo < min_kilo:
            min_kilo = kilo
            min_kilo_ad = kilo
            min_kilo_soyad = kilo
    else:
        print("Kazanamadınız.")

    devam = input("Devam etmek istiyor musunuz e/h:")

print(f"En uzun kişi: {ad} {soyad}, boyu: {boy} m")
print(f"En zayıf kişi: {ad} {soyad}, kilosu: {kilo} kg")