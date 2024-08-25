X_MIN = -3
X_MAX = 3
Y_MIN = -3
Y_MAX = 3

f_toplam = 0
gecersiz_sayi = 0

for x in range(X_MIN, X_MAX+1):
    for y in range(Y_MIN, Y_MAX+1):
        if x + y != gecersiz_sayi:
            f = (2*x + 3*y - 4*x*y +5) / (x + y)
            print(f"f({x},{y}) = {f}")
            f_toplam += f
        else:
            print(f"f({x},{y}) için sonuç tanımsız.")
            gecersiz_sayi += 1

print(f"Fonksiyon değerlerinin ortalaması : {f_toplam / (X_MAX - X_MIN +1) * (Y_MAX - Y_MIN +1) - gecersiz_sayi}")