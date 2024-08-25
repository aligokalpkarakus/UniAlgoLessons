#   1-10 arasında kodlanmış 10 satıcının çalıştığı bir mağazada haftanın 7 günü boyunca satıcıların her yaotığı satış
# için satıcı kodu ve satış tutarı verilerini alan, satıcıların günlük satış toplamlarını, mağazanın satıcı ve gün
# bazında satış toplamlarını ve haftalık satış toplamını bulan algoritma:

satislar = []

for sat_no in range(10):
    hafta = [0] * 7
    satislar.append(hafta)

for gun_no in range(7):
    devam = 'e'
    while devam == 'e':
        satici_no = int(input("Satıcı no giriniz:"))
        tutar = int(input("Tutar:"))
        satislar[satici_no-1][gun_no] += tutar
        devam = input("Devam:")

    genel_top = 0
    gun_top = [0] * 7
    for satici_no in range(10):
        satici_top = 0
        for gun_no in range(7):
            print(satislar[satici_no][gun_no])
            satici_top += satislar[satici_no][gun_no]
            gun_top[gun_no] += satislar[satici_no][gun_no]
        print(sum(satislar[satici_no]))

    for gun_no in range(7):
        print(gun_top[gun_no])
        genel_top += gun_top[gun_no]
    print(sum(gun_top))