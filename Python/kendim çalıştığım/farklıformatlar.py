bolunen = int(input("Bölünen sayıyı giriniz : "))
bolen = int(input("Bölen sayıyı giriniz : "))

sablon = f"{bolunen} sayısı {bolen} sayısına tam"

if  bolunen % bolen == 0 :
    print(sablon, "bölünüyor.")
else :
    print(sablon, "bölünmüyor.")

#2. yol formatı farklı kullanma

bolunen = int(input("Bir sayı girin: "))
bolen = int(input("Bir sayı daha girin: "))

ssablon = "{} sayısı {} sayısına tam".format(bolunen, bolen)

if bolunen % bolen == 0:
    print(ssablon, "bölünüyor!")
else:
    print(ssablon, "bölünmüyor!")