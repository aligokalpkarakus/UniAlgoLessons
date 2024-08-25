kullanilan_izin = int(input("Kaç gün izin kullandığınızı giriniz : "))
ayin_elemani_secildi  = (input("Ayın elemanı seçilip seçilmediğinizi (e/h) giriniz : "))

if kullanilan_izin > 0 or ayin_elemani_secildi == 'h':
    print("Tatil kazanma hakkınız yoktur.")
else:
    unvan = input("Unvanınızı giriniz : ")
    cal_yil_sayisi = int(input("Kaç yıl çalıştığınızı giriniz : "))
    if unvan == 'stajyer':
        tatil_yeri = 'Türkiye'
    elif unvan == 'uzman':
        tatil_yeri = 'Avrupa'
    elif unvan == 'takım lideri':
        tatil_yeri = 'Uzak Doğu'
    else:
        tatil_yeri = 'Amerika'

    if cal_yil_sayisi < 2:
        tatil_gun_sayisi = 3
    elif 2 <= cal_yil_sayisi < 5:
        tatil_gun_sayisi = 4
    elif 5 <= cal_yil_sayisi < 10:
        tatil_gun_sayisi = 5
    else:
        tatil_gun_sayisi = 7
    print(f"Tebrikler! {tatil_gun_sayisi} günlük {tatil_yeri} tatilini kazandınız. ")