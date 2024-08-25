#Problem:
# Özel bir üniversite tüm öğrencilerine aylık 450 TL burs vermektedir. Ayrıca 
# üniversite, not ortalaması 4 üzerinden en az 2 olan tüm öğrencilere not ortalamasının 
# 55 katı kadar ve ailesinin aylık geliri asgari ücretin (5500 TL) altında olan kız 
# öğrencilere 250 TL ek burs vermektedir. Buna göre bir öğrencinin adını soyadını, 
# 4 üzerinden not ortalamasını, cinsiyetini (e/k) ve kız ise ailesinin aylık 
# gelirini kullanıcıdan alan (hata kontrolüne gerek yoktur) ve öğrencinin alacağı 
# aylık burs miktarını hesaplayarak ekrana yazdıran bir algoritma ve program yazınız.


#Algoritma:
#TABAN_BURS=450
#EK_BURS_MIN_NOT=2
#EK_BURS_NOT_CARPANI=55
#ASGARI_UCRET=5500
#KIZ_EK_BURS=250
#
#ad_soyad=input()
#not_ort=input()
#cinsiyet=input()
#if cinsiyet=="k":
#    aylik_gelir=input()
#
#burs=TABAN_BURS
#if cinsiyet=="k" and aylik_gelir<ASGARI_UCRET:
#    burs=burs+KIZ_EK_BURS
#
#if not_ort>=EK_BURS_MIN_NOT:
#    burs=burs+not_ort*EK_BURS_NOT_CARPANI
#
#print(burs)


#Program:
TABAN_BURS=450
EK_BURS_MIN_NOT=2
EK_BURS_NOT_CARPANI=55
ASGARI_UCRET=5500
KIZ_EK_BURS=250

ad_soyad=input("adınızı soyadınızı giriniz:")
not_ort=float(input("not ort giriniz:"))
cinsiyet=input("cinsiyetinizi giriniz(e/k):")
if cinsiyet=="k":
    aylik_gelir=float(input("ailenizin aylık gelirini giriniz:"))

burs=TABAN_BURS
if cinsiyet=="k" and aylik_gelir<ASGARI_UCRET:
    burs=burs+KIZ_EK_BURS

if not_ort>=EK_BURS_MIN_NOT:
    burs=burs+not_ort*EK_BURS_NOT_CARPANI

print(f"Sayın {ad_soyad}, alacağınız aylık burs miktarı: {burs:.2f} TL")
