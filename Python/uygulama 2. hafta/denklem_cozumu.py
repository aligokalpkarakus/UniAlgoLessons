#Problem:
# ax+b=c şeklinde verilen bir lineer denklem
# aşağıdaki formül kullanılarak çözülebilir:
#
# x=(c-b)/a
#
# Buna göre (a,b,c) sayılarını kullanıcıdan alan ve x’in değerini bularak
# ekrana yazdıran bir program yazınız.


#Program:
a=int(input("a sayısını giriniz:"))
b=int(input("b sayısını giriniz:"))
c=int(input("c sayısını giriniz:"))

x=(c-b)/a

print("x=",x)
