import cember
import kuvvet
import math

cevre = cember.cember_cevre()  # r = 1 pi = 3.14
print(f"Çemberin çevresi: {cevre}")

cevre = cember.cember_cevre(5)  # r = 5 pi = 3.14
print(f"Çemberin çevresi: {cevre}")

cevre = cember.cember_cevre(5, 3)  # r = 5 pi = 3
print(f"Çemberin çevresi: {cevre}")

cevre = cember.cember_cevre(pi=3, r=5)  # isimlerle verildiği sürece aynı çıkar
print(f"Çemberin çevresi: {cevre}")

r = float(input("Yariçap ="))
cevre = cember.cember_cevre(r)
print(f"Çemberin çevresi: {cevre}")

cevre = cember.cember_cevre(r, math.pi)
print(f"Çemberin çevresi: {cevre}")

print(f"2 üzeri 16 = {kuvvet.uslu_sayi(2,16)}")
print(f"111 üzeri 0 = {kuvvet.uslu_sayi(111,0)}")
print(f"2 üzeri 10 = {kuvvet.uslu_sayi(kuvvet=10, taban=2)}")

tabann = int(input("Taban:"))
kuvvett = int(input("Kuvvet:"))

print(f"{tabann} üzeri {kuvvett} = {kuvvet.uslu_sayi(tabann,kuvvett)}")
print(f"{tabann} üzeri {kuvvett} = {kuvvet.uslu_sayi(kuvvet=kuvvett,taban=tabann)}")