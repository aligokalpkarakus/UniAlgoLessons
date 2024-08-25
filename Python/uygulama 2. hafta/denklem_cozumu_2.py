#Problem:
# ax+b=c şeklinde verilen bir lineer denklem
# aşağıdaki formül kullanılarak çözülebilir:
#
# x=(c-b)/a
#
# Buna göre (a,b,c) sayılarını kullanıcıdan alan ve x’in değerini bularak
# ekrana yazdıran bir program yazınız.


#Program:
a=float(input("a sayısını giriniz:"))
b=float(input("b sayısını giriniz:"))
c=float(input("c sayısını giriniz:"))

if a==0:
    print("Sonuç yok!")
else:
    x=(c-b)/a
    print("x=",x)
