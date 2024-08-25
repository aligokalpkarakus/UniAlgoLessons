# [0-100] arasındaki çift sayıların toplamı

# 1. yol
toplam = 0
sayi = 2

while sayi <= 100:
    toplam += sayi
    sayi += 2
print(toplam)

# 2. yol

toplam = 0

for sayac in range(2,101,2):
    toplam += sayi
print(toplam)
