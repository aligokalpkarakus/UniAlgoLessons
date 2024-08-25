
devam = 'e' or 'E'

bilye_sayisi = int(input("Bilye sayısı:"))
while devam in ['e', 'E']:

    birinci_bilye_agirligi = int(input("1. bilyenin ağırlığını giriniz:"))
    birinci_bilye_sayac = 0
    ikinci_bilye_agirligi = int(input("2. bilyenin ağırlığını giriniz:"))
    ikinci_bilye_sayac = 0

    if birinci_bilye_agirligi == ikinci_bilye_agirligi:
        birinci_bilye_sayac += 2
    else:
        birinci_bilye_sayac += 1
        ikinci_bilye_sayac += 1

    for bilye_no in range(3, bilye_sayisi+1):
        bilye_agirligi = int(input(f"{bilye_no}. bilyenin ağırlığını giriniz:"))
        if birinci_bilye_agirligi == bilye_agirligi:
            birinci_bilye_sayac += 1
        if birinci_bilye_agirligi != ikinci_bilye_agirligi and bilye_agirligi == birinci_bilye_agirligi:
            birinci_bilye_sayac += 1
        if ikinci_bilye_agirligi != birinci_bilye_agirligi and bilye_agirligi == ikinci_bilye_agirligi:
            ikinci_bilye_agirligi += 1

        if birinci_bilye_sayac >= 2 and ikinci_bilye_sayac >= 2:
            print("hatalı kutu")
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

