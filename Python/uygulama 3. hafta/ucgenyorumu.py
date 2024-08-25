uzun_kenar = int(input("Uzun kenarın uzunluğunu giriniz : "))
kisa_kenar1 = int(input("Kısa kenarın uzunluğunu giriniz : "))
kisa_kenar2 = int(input("Kısa kenarın uzunluğunu giriniz : "))

if uzun_kenar >= kisa_kenar1 + kisa_kenar2 :
    print("Üçgen değil.")
else:
    uzun_kenar_kare = uzun_kenar ** 2
    kisa_kenar_kare_top = kisa_kenar_1 ** 2 + kisa_kenar_2 ** 2
    if uzun_kenar_kare == kisa_kenar_kare_top:
        print("Dik üçgen.")
    elif uzun_kenar_kare > kisa_kenar_kare_top:
        print("Geniş açılı üçgen.")
    else:
        print("Dar açılı üçgen.")