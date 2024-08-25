def sayi_al(alt_sinir, ust_sinir):
    sayi = int(input())
    while not alt_sinir <= sayi <= ust_sinir:
        sayi = int(input("Hatalı sayı girdiniz. Lütfen tekrar giriniz:"))
    return sayi


def dikdortgen_ciz(dikey_kenar, yatay_kenar):
    for i in range(dikey_kenar):
        for j in range(yatay_kenar):
            print('*', end='')
        print('')


def dikdortgen_bilgilerini_hesapla(kenar1, kenar2):
    return kenar1 * kenar2, 2 * (kenar1 + kenar2), kenar1 == kenar2


def faktoriyel(sayi):
    carpim = 1
    for i in range(sayi, 1, -1):
        carpim *= i
    return carpim


def kombinasyon(n, k):
    return int(faktoriyel(n) / (faktoriyel(k) * faktoriyel(n-k)))


def menu_goruntule():
    print("1. Dikdörtgen çizme..")
    print("2. Dikdörtgen bilgilerini hesaplama..")
    print("3. Faktöriyel hesaplama..")
    print("4. Kombinasyon hesaplama..")
    print("0. Çıkış..")


def main():
    cikis = 'h'
    while cikis == 'h' or cikis == 'H':
        menu_goruntule()
        print("Seçiminizi giriniz. [0-4]: ", end='')
        secim = sayi_al(0, 4)

        if secim == 1:
            print("Dikdörtgenin dikey dikey uzunluğunu giriniz [1,20]: ", end='')
            dikey_kenar = sayi_al(1, 20)
            print("Dikdörtgenin yatay kenar uzunluğunu giriniz [1,75]: ", end='')
            yatay_kenar = sayi_al(1, 75)
            dikdortgen_ciz(dikey_kenar, yatay_kenar)

        elif secim == 2:
            print("1. kenara ait uzunluğu giriniz [1,1000]: ", end='')
            kenar1 = sayi_al(1, 1000)
            print("2. kenara ait uzunluğu giriniz [1,1000]: ", end='')
            kenar2 = sayi_al(1, 1000)
            alan, cevre, kare = dikdortgen_bilgilerini_hesapla(kenar1, kenar2)
            print(f"Dikdörtgenin alanı: {alan}, çevresi: {cevre}")
            if kare:
                print("Bu dikdörtgen bir karedir.")

        elif secim == 3:
            print("Faktörileyi hesapalanacak olan sayıyı giriniz [1,10]: ", end='')
            faksayi = sayi_al(1, 10)
            print(f" {faksayi}! = {faktoriyel(faksayi)}")

        elif secim == 4:

            print("n sayısını giriniz [1-10]: ", end='')
            n = sayi_al(1, 10)
            print("k sayısını giriniz [1,n]", end='')
            k = sayi_al(1, n)
            print(f"C({n},{k}) = {kombinasyon(n, k)}")
        else:
            cikis = input("Çıkış yapmak istediğinizden emin misiniz: ")
            while cikis not in ['e', 'E', 'h', 'H']:
                cikis = input("Hatalı veri girişi. Tekrar deneyiniz.")


main()
