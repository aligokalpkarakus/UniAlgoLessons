# Girilecek 100 adet (x,y) değerleri için denkemi aşağıda görülen f(x,y) fonksiyonunun max ve min değerlerini bulan
# algoritma

def f1(x, y):
    return -(x**2) + 3*(y**2) - 4*x*y + 5


x = int(input("x:"))
y = int(input("y:"))
sonuc = f1(x, y)
max = sonuc
min = sonuc

for sayac in range(99):
    x = int(input("x:"))
    y = int(input("y:"))
    sonuc = f1(x, y)
    if sonuc > max:
        max = sonuc
    elif sonuc < min:
        min = sonuc
print(f"Maksimum sonuç: {max}\nMinimum sonuç: {min}")
