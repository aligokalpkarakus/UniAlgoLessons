MIN_BILYE = 10
MIN_AGIRLIK = 0
FARKLI_SINIR = 1

devam = 'e' or 'E'

while devam in ['e', 'E']:
    bilye_sayisi = int(input("Bilye sayısını giriniz (10 veya 10'dan fazla olmalı):"))
    guncel_deger = 0
    farkli_bilye_sayaci = 0
    while bilye_sayisi < MIN_BILYE:
        bilye_sayisi = int(input("Hatalı giriş yaptınız. Lütfen 10 veya 10'dan fazla adet giriniz:"))
    else:
        bilye_agirligi1 = int(input("1. bilyenin ağırlığını giriniz (mg cinsinden pozitif değer giriniz):"))
        if bilye_agirligi1 <= 0:
            bilye_agirligi1 = int(input("Hatalı giriş yaptınız. Lütfen pozitif değer giriniz:"))

        bilye_agirligi2 = int(input("2. bilyenin ağırlığını giriniz (mg cinsinden pozitif değer giriniz):"))
        if bilye_agirligi2 <= 0:
            bilye_agirligi2 = int(input("Hatalı giriş yaptınız. Lütfen pozitif değer giriniz:"))

        bilye_agirligi3 = int(input("3. bilyenin ağırlığını giriniz (mg cinsinden pozitif değer giriniz):"))
        if bilye_agirligi3 <= 0:
            bilye_agirligi3 = int(input("Hatalı giriş yaptınız. Lütfen pozitif değer giriniz:"))

        if bilye_agirligi1 == bilye_agirligi2 and bilye_agirligi1 == bilye_agirligi3:
            kutudaki_bilyenin_agirligi = bilye_agirligi1

        elif bilye_agirligi1 != bilye_agirligi2 and bilye_agirligi1 == bilye_agirligi3:
            farkli_bilye_sayaci += 1

        elif bilye_agirligi1 == bilye_agirligi2 and bilye_agirligi1 != bilye_agirligi3:
            farkli_bilye_sayaci += 1



        for bilye_no in range(4, bilye_sayisi + 1):
            bilye_agirligi = int(input(""))
            while bilye_agirligi  <= 0:
                bilye_agirligi = int(input("Hatalı giriş yaptınız. Lütfen ağırlığı pozitif değer giriniz:"))
            else:
                guncel_agirlik = bilye_agirligi




    devam = input("Devam etmek için e/E, bitirmek için h/H giriniz:")
    if devam in ['h', 'H']:
        print("Girişler tamamlandı.")
        break
    elif devam in ['e', 'E']:
        continue
    else:
        devam = input("Hatalı giriş yaptınız. Devam etmek için e/E, bitirmek için h/H giriniz:")
