# Problem:
# Önce bugün ayın kaçıncı günü olduğunu, sonra da ayın her günü için metrekareye düşen yağmur miktarını (kg)
# kullanıcıdan alan (hata kontrolüne gerek yoktur) ve o aya ilişkin aşağıdaki
# istatistiksel bilgileri ekrana yazdıran bir algoritma ve program yazınız.
#
# - Yağmurlu gün sayısı ve yüzdesi
# - Günlük ortalama yağmur miktarı (kg)


#Algoritma:
#gun_sayisi=input()
#
#yagmurlu_gun_sayisi=0
#yagmur_miktari_toplami=0
#
#for gun_no in range(1,gun_sayisi+1):
#    print(gun_no)
#    yagmur_miktari=input()
#
#    yagmur_miktari_toplami += yagmur_miktari
#    if yagmur_miktari>0:
#        yagmurlu_gun_sayisi+=1
#
#print(yagmurlu_gun_sayisi,yagmurlu_gun_sayisi*100/gun_sayisi)
#print(yagmur_miktari_toplami/gun_sayisi)


#Program:
gun_sayisi=int(input("Bugün ayın kaçıncı günü?"))

yagmurlu_gun_sayisi=0
yagmur_miktari_toplami=0

for gun_no in range(1,gun_sayisi+1):
    yagmur_miktari=float(input(f"{gun_no}. günün yağmur miktarını giriniz(kg):"))

    yagmur_miktari_toplami += yagmur_miktari
    if yagmur_miktari>0:
        yagmurlu_gun_sayisi+=1

print(f"Yağmurlu gün sayısı: {yagmurlu_gun_sayisi} ve yüzdesi: %{yagmurlu_gun_sayisi*100/gun_sayisi:.2f}")
print(f"Günlük ortalama yağmur miktarı: {yagmur_miktari_toplami/gun_sayisi:.2f} kg")
