# bir bölme işleminde hem bölümü hem kalanı döndüren fonksiyon

def tam_bolme(bolunen,bolen):
    return bolunen // bolen and bolunen % bolen

bolum,kalan = tam_bolme(8,5)