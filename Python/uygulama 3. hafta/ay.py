ay_no = int(input("Kaçıncı ay olduğunu giriniz (1-12) : "))

if ay_no < 1 or ay_no > 12:
    print("Hatalı giriş yaptınız.")
else:
    if ay_no == 2:
        print("28 gün")
    elif ay_no == 4 or ay_no == 6 or ay_no == 9 or ay_no == 11:
        print("30 gün")
    else:
        print("31 gün")
