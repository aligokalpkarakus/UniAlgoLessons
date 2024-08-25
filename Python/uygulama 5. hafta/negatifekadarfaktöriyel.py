sayi = int(input("Sayı:"))

while not sayi < 0:
    faktoriyel = 1
    for carpan in range(sayi,1,-1):
        faktoriyel *= carpan
    print(sayi,"! =",faktoriyel)

    sayi = int(input("Sayı:"))