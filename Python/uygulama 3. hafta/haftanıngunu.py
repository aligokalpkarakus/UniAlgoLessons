# Haftanın kaçıncı günü olduğunu alan ve gün adı ile hafta içi olup olmadığını yazdıran algoritma:

gun_no = int(input("Günün sayısını giriniz : "))

if 1 <= gun_no <= 7:
    if gun_no <= 5:
        if gun_no == 1:
            print("Pazartesi")
        elif gun_no == 2:
            print("Salı")
        elif gun_no == 3:
            print("Çarşamba")
        elif gun_no == 4:
            print("Perşembe")
        else:
            print("Cuma")
        print("Hafta içi")
    else:
        if gun_no == 6:
            print("Cumartesi")
        else:
            print("Pazar")
        print("Haftasonu")
else:
    print("Hatalı giriş yaptınız")
