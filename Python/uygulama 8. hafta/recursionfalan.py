global_degisken = 27
global_sayac=0

def bir_fonksiyon():
    global global_degisken
    global_degisken = global_degisken + 1

def dis_fonksiyon(dis_parametre = 123):
    dis_degisken = global_degisken + dis_parametre

    def ic_fonksiyon(ic_parametre = 0):
        ic_degisken = ic_parametre + dis_degisken + global_degisken
        return ic_degisken

    sonuc = ic_fonksiyon(dis_degisken)
    return sonuc

def fibonacci(sayi):
    global global_sayac
    global_sayac+=1
    if sayi==1 or sayi==2:
        return 1
    else:
        onceki=fibonacci(sayi-1)
        iki_onceki=fibonacci(sayi-2)
        #print(f"{sayi-1}. fibonacci sayisi: {onceki}")
        print(f"{sayi-2}. fibonacci sayisi: {iki_onceki}")
        print(f"{sayi-1}. fibonacci sayisi: {onceki}")
        return onceki+iki_onceki

sonuc  = dis_fonksiyon(7)
print(f'Sonuç: {sonuc}')

bir_fonksiyon()

sonuc  = dis_fonksiyon(7)
print(f'Sonuç: {sonuc}')

sonuc  = dis_fonksiyon()
print(f'Sonuç: {sonuc}')

print(f"7. fibonacci sayisi: {fibonacci(7)}")
print(f'Global sayac: {global_sayac}')