# girilen bir sayının faktöriyelini bulma

# 1. yol
n = int(input("Bir sayı giriniz : "))

faktoriyel = 1

for sayi in range(n, 0, -1):
    faktoriyel *= sayi
print(faktoriyel)

# 2. yol

n = int(input("Bir sayı giriniz : "))
faktoriyel = 1
sayi = n

while sayi > 1:
    faktoriyel *= sayi
    sayi -= 1
print(faktoriyel)

