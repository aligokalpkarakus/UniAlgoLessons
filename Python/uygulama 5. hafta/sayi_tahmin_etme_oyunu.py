# Problem:
# Bilgisayarın tuttuğu sayıyı tahmin etme oyunu oynamaya yarayan bir algoritma ve program yazınız.
# Bilgisayar 1-100 arasında rasgele bir sayı tutacak ve kullanıcı bu sayıyı en az tahmin ile bulmaya çalışacaktır.
# Bunun için bilgisayar kullanıcıyı “YUKARI” ve “AŞAĞI” mesajları ile yönlendirmelidir.
# Kullanıcı sayıyı bulduğunda “TEBRİKLER” mesajı verilerek sayıyı kaç tahminde bulduğu belirtilmelidir.


#Algoritma:
#MIN_SAYI=1
#MAX_SAYI=100
#
#sayi=randint(MIN_SAYI,MAX_SAYI) # randint(min,max) fonksiyonu, min ile max arasında rasgele bir tamsayı döndürür.
#
#tahmin=input()
#tahmin_say=1
#
#while (sayi!=tahmin):
#    if tahmin<sayi:
#        print("YUKARI!")
#    else:
#        print("AŞAĞI!")
#
#    tahmin=input()
#    tahmin_say+=1
#
#print("TEBRİKLER!")
#print(tahmin_say)


#Program:
import random # random kütüphanesi, rasgele sayı üretimi ile ilgili hazır fonksiyonları içerir.

MIN_SAYI=1
MAX_SAYI=100

sayi=random.randint(MIN_SAYI,MAX_SAYI) # randint(min,max) fonksiyonu, min ile max arasında rasgele bir tamsayı döndürür.

tahmin=int(input("Lütfen tahmini bir sayı giriniz:"))
tahmin_say=1

while (sayi!=tahmin):
    if tahmin<sayi:
        print("YUKARI!")
    else:
        print("AŞAĞI!")

    tahmin=int(input("Lütfen tahmini bir sayı giriniz:"))
    tahmin_say+=1

print("TEBRİKLER! Doğru tahmin ettiniz.")
print(f"{tahmin_say} tahminde bilgisayarın tuttuğu sayıyı buldunuz.")
