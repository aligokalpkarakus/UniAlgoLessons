#parametre olarak verilen bir taban sayısının, yine parametre olarak verilen bir kuvvetini hesaplayıp geri döndüren
# özyinelemeli (recursive) bir fonksiyon yazınız. daha sonra bu fonksiyonu kaydediniz. kuvvet.py

def uslu_sayi(taban,kuvvet):
    if kuvvet == 0:
        return 1
    else:
        return taban*uslu_sayi(taban,kuvvet-1)
    