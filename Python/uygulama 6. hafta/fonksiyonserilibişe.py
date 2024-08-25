# aşağıda görülen f(x) serisinin terim sayısınıve x değerini kullanıcıdan alan ve serinin değerini bulan algoritma
# x - x**3/3! + x**5/5! - ... (-1)**(n+1)*(x**(2n-1))/(2n-1)!

def kuvvetini_bul(taban,us):
    kuvvet = 1
    for sayac in range(us):
        kuvvet *= taban
    return kuvvet

def faktoriyeli_bul(sayi):
    faktoriyel = 1
    for carpan in range(sayi,1,-1):
        faktoriyel *= carpan
    return faktoriyel

def main():
    x = int(input("x:"))
    terim_sayisi = int(input("terim:"))
    seri_top = 0

    for n in range(1,terim_sayisi+1):
        seri_top += kuvvetini_bul(-1, n+1) * kuvvetini_bul(x, n-1) / faktoriyeli_bul(2*n-1)

    print(seri_top)
main()