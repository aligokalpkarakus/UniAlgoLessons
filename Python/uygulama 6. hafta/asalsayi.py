sayi = int(input("Sayı giriniz:"))

while sayi > 1:
    for bolen in range(2, int(sayi**0.5) +1):
        if sayi % bolen == 0:
            print(f"{sayi} asal sayı değildir.")
            break
    else:
        print(f"{sayi} asal sayıdır.")

    sayi = int(input("Sayı giriniz:"))


