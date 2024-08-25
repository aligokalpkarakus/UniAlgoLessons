#   Girilen bir metindeki türkçede er alan 29 harfin tekrar sayılarını küçük, büyük harf ayrımı olmadan bulan algoritma

metin = input("Metin giriniz:")
alfabe = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"

def buyuk_harf(metin):
    buyuk_metin = ""
    for kar in metin:
        if kar == 'i':
            buyuk_metin += "İ"
        else:
            buyuk_metin += kar.upper()
    return buyuk_metin

"""harf_say = [0] * 29

for kar in metin:
    konum = alfabe.find(kar)
    if konum != -1:
        harf_say[konum] += 1
for i in range(29):
    print(alfabe[i], harf_say[i])"""

"""harf_say = {harf : 0 for harf in alfabe}
for kar in metin:
    if kar in alfabe:
        harf_say[kar] += 1
for kar in harf_say:
    print(kar,harf_say[kar])"""

for harf in alfabe:
    print(harf, metin.count(harf))