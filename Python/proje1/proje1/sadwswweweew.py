
devam = 'e' or 'E'

bilye_sayisi = int(input("Bilye sayısı:"))
while devam in ['e', 'E']:
    birinci_bilye_agirligi = 0
    birinci_bilye_sayac = 0
    ikinci_bilye_agirligi = 0
    ikinci_bilye_sayac = 0
    farkli_deger = 0
    farkli_deger_sayac = 0

    for bilye_no in range(1, bilye_sayisi+1):
        bilye_agirligi = int(input(f"{bilye_no}. bilye ağırlığı:"))
        if bilye_no == 1:
            birinci_bilye_sayac += 1
            birinci_bilye_agirligi = bilye_agirligi
        if bilye_no > 1 and bilye_agirligi == birinci_bilye_agirligi:
            birinci_bilye_sayac += 1
        if bilye_agirligi != birinci_bilye_agirligi:
            ikinci_bilye_agirligi = bilye_agirligi
            ikinci_bilye_sayac += 1
        if bilye_agirligi == ikinci_bilye_agirligi:
            ikinci_bilye_sayac += 1
        if (bilye_agirligi != birinci_bilye_agirligi and bilye_agirligi != ikinci_bilye_agirligi) or (
                birinci_bilye_sayac >= 2 and ikinci_bilye_sayac >= 2):
            print("Hatalı")
            break
    print(birinci_bilye_sayac)
    print(ikinci_bilye_sayac)

    devam = input("Devam mı:")
    if devam not in ['e', 'E', 'h', 'H']:
        devam = input("Hatalı giriş. Lütfen devam etmek için e/E, çıkış için h/H giriniz:")
    else:
        if devam in ['h', 'H']:
            print("Girişler bitti...")
        else:
            print("Yeni kutu girişi...")
            bilye_sayisi = int(input("Bilye sayısı:"))

