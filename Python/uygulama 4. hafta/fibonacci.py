# fibonacci sayısının algoritması, n. fibonacci sayısını bul

n = int(input("Kaçıncı olsun : "))
iki_onceki = int(input("İki önceki sayı kaç olsun : "))
bir_onceki = int(input("Bir önceki sayı kaç olsun : "))

for sayac in range(3, n+1):
    fibonacci_n = iki_onceki + bir_onceki
    iki_onceki = bir_onceki
    bir_onceki = fibonacci_n
