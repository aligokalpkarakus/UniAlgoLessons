fonye = open('fonye.txt')
veri = input(fonye)
min = veri
max = veri

while veri!="":
    if veri > max:
        max = veri
    elif veri < min:
        min = veri
    veri = input(fonye)

print(max,veri)