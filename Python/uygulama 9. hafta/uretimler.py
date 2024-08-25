# Problem:
# Bir fabrikada üretim yapan makinalar 1’den başlayarak numaralanmışlardır. Bazı makinalar bazı
# günler üretim dışı (bakım ya da arıza nedeniyle) kalabilmektedir. Bir ay boyunca makinaların
# üretim yaptıkları her gün için gün numarası, makina numarası ve günlük üretim miktarı verileri
# “aylik_uretim.txt” isimli bir dosyada biriktirilmiştir. Dosyanın her satırında yalnız 1 veri elemanı
# ve ilk satırında da fabrikadaki makine sayısı verisi bulunmaktadır (örnek bir veri dosyası ekte
# verilmiştir). Buna göre, bu dosyadaki verileri kullanarak her makinanın aylık toplam üretim miktarı
# ve günlük üretim ortalaması (sadece üretim yaptıkları gün sayısına göre) bilgilerini; ayrıca
# fabrikanın aylık toplam üretim miktarı, aylık toplam üretim miktarı en yüksek olan makinanın numarası
# ve üretim miktarı bilgilerini aşağıdaki gibi ekranda listeleyen bir algoritma ve program yazınız:
#
#Makina No   Aylık Üretim   Üretim Yaptığı Gün Sayısı   Günlük Ortalama
#---------   ------------   -------------------------   ---------------
#...         ...            ...                         ...
#
#Fabrikanın aylık üretimi: ...
#Aylık üretimi en yüksek olan makinanın numarası: ...
#Aylık üretimi en yüksek olan makinanın aylık üretimi: ...


#Algoritma:
#def uretim_verilerini_al(uretim_dosyasi,uretim_toplamlari,gun_sayilari):
#    gun_no=uretim_dosyasi.readline()
#    while gun_no!="":
#        makina_no=uretim_dosyasi.readline()
#        gunluk_uretim=uretim_dosyasi.readline()
#        uretim_toplamlari[makina_no-1]+=gunluk_uretim
#        gun_sayilari[makina_no-1]+=1
#        gun_no=uretim_dosyasi.readline()
#
#def istatistikler(uretim_toplamlari,gun_sayilari,makina_say):
#    for makina_no in range(makina_say):
#        print(makina_no+1)
#        print(uretim_toplamlari[makina_no])
#        print(gun_sayilari[makina_no])
#        if gun_sayilari[makina_no]!=0:
#            print(uretim_toplamlari[makina_no]/gun_sayilari[makina_no])
#        else:
#            print(0)
#
#    print(sum(uretim_toplamlari))
#    max_uretim=max(uretim_toplamlari)
#    max_no=uretim_toplamlari.index(max_uretim)+1
#    print(max_no)
#    print(max_uretim)
#
#def main():
#    uretim_dosyasi=open("aylik_uretim.txt","r")
#    makina_say=uretim_dosyasi.readline()
#    uretim_toplamlari=[0]*makina_say
#    gun_sayilari=[0]*makina_say
#    uretim_verilerini_al(uretim_dosyasi,uretim_toplamlari,gun_sayilari)
#    uretim_dosyasi.close()
#    istatistikler(uretim_toplamlari, gun_sayilari,makina_say)
#
#main()


#Program:
def uretim_verilerini_al(uretim_dosyasi,uretim_toplamlari,gun_sayilari):
    gun_no=uretim_dosyasi.readline()
    while gun_no!="":
        makina_no=int(uretim_dosyasi.readline())
        gunluk_uretim=int(uretim_dosyasi.readline())
        uretim_toplamlari[makina_no-1]+=gunluk_uretim
        gun_sayilari[makina_no-1]+=1
        gun_no=uretim_dosyasi.readline()

def istatistikler(uretim_toplamlari,gun_sayilari,makina_say):
    print("Makina No   Aylık Üretim   Üretim Yaptığı Gün Sayısı   Günlük Ortalama")
    print("---------   ------------   -------------------------   ---------------")
    for makina_no in range(makina_say):
        print(f"{makina_no+1:9d}",end="   ")
        print(f"{uretim_toplamlari[makina_no]:12d}",end="   ")
        print(f"{gun_sayilari[makina_no]:25d}",end="   ")
        try:
            print(f"{uretim_toplamlari[makina_no]/gun_sayilari[makina_no]:15.2f}")
        except ZeroDivisionError:
            print(f"{0.00:15.2f}")

    print(f"\nFabrikanin aylık üretimi: {sum(uretim_toplamlari)}")
    max_uretim=max(uretim_toplamlari)
    max_no=uretim_toplamlari.index(max_uretim)+1
    print(f"Aylık üretimi en yüksek olan makinanın numarası: {max_no}")
    print(f"Aylık üretimi en yüksek olan makinanın aylık üretimi: {max_uretim}")

def main():
    try:
        uretim_dosyasi = open("aylik_uretim.txt", "r")
        makina_say = int(uretim_dosyasi.readline())
        uretim_toplamlari = [0] * makina_say
        gun_sayilari = [0] * makina_say
        uretim_verilerini_al(uretim_dosyasi, uretim_toplamlari, gun_sayilari)
        uretim_dosyasi.close()
        istatistikler(uretim_toplamlari, gun_sayilari,makina_say)
    except IOError:
        print("Veri dosyası açılamadı ya da okunamadı!")

main()
