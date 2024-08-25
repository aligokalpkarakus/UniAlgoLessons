# Erkekler için boy  sınırı 175 kilo sıınrı 75, kızlar için boy 165 kilo 65 sınır olan askeri sınava kabul

E_BOY_BARAJ = 175
E_KILO_BARAJ = 75
K_BOY_BARAJ = 165
K_KILO_BARAJ = 65

boy = int(input("Boyunuzu giriniz : "))
kilo = int(input("Kilonuzu giriniz : "))
cins = input("Cinsiyetinizi giriniz : ")

if cins == 'e' or cins == 'E' :
    if boy >= E_BOY_BARAJ and kilo <= E_KILO_BARAJ :
        print("Kabul edildiniz.")
    else:
        print("Kabul edilmediniz.")
else:
    if cins == 'k' or cins == 'K' :
        if boy >= K_BOY_BARAJ and kilo <= K_KILO_BARAJ :
            print("Kabul edildiniz.")
        else:
            print("Kabul edilmediniz.")
    else:
        print("Hatalı giriş yaptınız.")