def sayi_al(alt_sinir,ust_sinir): # parametre alan ve deger donduren fonksiyon ornegi
    sayi=int(input())
    while sayi<alt_sinir or sayi>ust_sinir: # sayi dogru girilinceye kadar bekleniyor...
        sayi=int(input("hatali veri girisi, lutfen tekrar giriniz:"))

    return sayi

def dikdortgen_ciz(dikey_kenar, yatay_kenar): # parametre alan ve deger dondurmeyen fonksiyon ornegi
    for i in range(dikey_kenar):
        for j in range(yatay_kenar):
            print('*',end='')
        print('')

def dikdortgen_bilgilerini_hesapla(kenar1, kenar2): # birden fazla deger donduren fonksiyon ornegi
    return kenar1*kenar2,2*(kenar1+kenar2),kenar1==kenar2

def faktoriyel(sayi):
    carpim=1
    for carpan in range(sayi,1,-1):
        carpim=carpim*carpan

    return carpim

def kombinasyon(n,k): # baska bir fonksiyon cagiran fonksiyon ornegi
    return int(faktoriyel(n)/(faktoriyel(k)*faktoriyel(n-k))) # faktoriyel fonksiyonu 3 kez cagriliyor...

def menu_goruntule(): # parametre almayan ve deger dondurmeyen fonksiyon ornegi
    print("1. Dikdortgen cizme...")
    print("2. Dikdortgen bilgilerini hesaplama...")
    print("3. Faktoriyel hesaplama...")
    print("4. Kombinasyon (C(n,k)) hesaplama...")
    print("0. Cikis...")

def main():
    cikis='h'
    while cikis=='H' or cikis=='h':
    #while cikis!='E' and cikis!='e': # ustteki satir, bu sekilde de yazilabilir
    #while not (cikis=='E' or cikis=='e'): # ustteki satir, bu sekilde de yazilabilir
        menu_goruntule() # programcinin kendisinin yazdigi fonksiyon cagriliyor...
        print("Seciminizi giriniz [0-4]:",end='') # kutuphane fonksiyonu cagriliyor...
        secim=sayi_al(0,4) # fonksiyon cagriliyor ve dondurdugu deger saklaniyor...

         # kullanicinin istegi yerine getiriliyor...
        if secim==1:
            print("Dikdortgenin dikey kenar uzunlugunu giriniz [1-20]:",end='')
            dikey_kenar=sayi_al(1,20)
            print("Dikdortgenin yatay kenar uzunlugunu giriniz [1-75]:",end='')
            yatay_kenar=sayi_al(1,75)
            dikdortgen_ciz(dikey_kenar,yatay_kenar) # fonksiyon cagriliyor, herhangi bir deger donmuyor...
        elif secim==2:
                print("Dikdortgenin bir kenarinin uzunlugunu giriniz [1-1000]:", end='')
                kenar1 = sayi_al(1,1000)
                print("Dikdortgenin diger kenarinin uzunlugunu giriniz [1-1000]:", end='')
                kenar2 = sayi_al(1,1000)
                alan,cevre,kare=dikdortgen_bilgilerini_hesapla(kenar1, kenar2)  # fonksiyon cagriliyor, 3 tane deger donuyor...
                print(f"Dikdörtgenin alanı: {alan} ve çevresi: {cevre}")
                if kare==True:
                    print("Bu dikdörtgen, bir karedir")
        elif secim==3:
            print("Faktoriyeli hesaplanacak sayiyi giriniz [0-10]:",end='')
            n=sayi_al(0,10)
            print(f"{n}!={faktoriyel(n)}") # fonksiyonun dondurdugu deger, baska bir fonksiyona parametre olarak gonderiliyor...
        elif secim==4:
            print("n sayisini giriniz [1-10]:",end='')
            n=sayi_al(1,10)
            print(f"k sayisini giriniz [1-{n}]:",end='')
            k=sayi_al(1,n)
            print(f"C({n},{k})={kombinasyon(n,k)}")
        else:
            cikis=input("Cikmak istediginize emin misiniz(e/E/h/H)?:")
            while cikis not in ['e', 'E', 'h', 'H']: # cevap dogru girilinceye kadar bekleniyor...
                cikis=input("hatali veri girisi, lutfen tekrar giriniz:")
    # while sonu

main()
