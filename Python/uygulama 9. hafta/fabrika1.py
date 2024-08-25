# bir fabrikadaki 1-10 arasında numaralanmış makinaların 30 günlük üretim verilerini gün numarasına göre
# sıralı olarak alan, her makinenin aylık üretim miktarını ve fabrikanın aylık üretim miktarını bulan algoritma:

mak_top = [0] * 10  # makina sayısı kadar bellekte yer açmak için
fab_top = 0

for gun_no in range(30):
    for mak_no in range(10):
        gunluk_uretim = int(input("Günlük üretimi giriniz:"))
        mak_top[mak_no] += gunluk_uretim
for mak_no in range(10):
    print(mak_top[mak_no])

print(sum(mak_top))