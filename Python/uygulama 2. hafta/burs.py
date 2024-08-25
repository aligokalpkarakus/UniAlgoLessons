TABAN_BURS = 450
MIN_NOT_ORT = 2
NOT_ORT_KATSAYI = 55
ASGARI_UCRET = 5500
EK_BURS = 250

ad_soyad = input("Adınızı soyadınızı giriniz : ")
not_ort = float(input("Not ortalamnızı giriniz : "))
cinsiyet = input("Cinsiyetinizi giriniz (e/k) : ")

if cinsiyet == 'k' :
    aile_gelir = int(input("Ailenizin aylık gelirini yazınız : "))

burs = TABAN_BURS

if not_ort >= MIN_NOT_ORT :
    burs = burs + not_ort * NOT_ORT_KATSAYI

if cinsiyet == 'k' and aile_gelir < ASGARI_UCRET :
    burs += EK_BURS

print(f"Sayın {ad_soyad}, alacağınız aylık burs miktarı : {burs:.2f} TL")