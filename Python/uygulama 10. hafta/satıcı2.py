# Bir mağazada çalışan satıcıların yaptıkları her satış için satıcı adı ve satış tutarı verilerini kullanıcıdan alan
# her satıcının yaptığı satışların toplam tutarını bulan algoritma.

satis_top = {}

devam = 'e'

while devam == 'e':
    satici_adi = input("Satıcı adı:")
    satis_tutari = int(input("Satış tutarı:"))

    satis_top[satici_adi] = satis_top.get(satici_adi,0) + satis_tutari
    devam = input("Devam:")
print(satis_top)