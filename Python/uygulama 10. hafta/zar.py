# yüzlerinde sarı,kırmızı,mavi,yeşil,mor, ve turuncu renkleri olan bir zarın 1000 kez atılması sonucunda gelen renkleri
# kullanıcıdan alan zarın yüzlerinde renklerin kaaçr kez geldiklerini bulan algoritma:

tekrar_say = {"SARI": 0, "KIRMIZI": 0, "MAVİ": 0, "YEŞİL": 0, "MOR": 0, "TURUNCU": 0}

for i in range(1000):
    yuz = input("Gelen rengi giriniz:")
    tekrar_say[yuz] += 1

for yuz in tekrar_say:
    print(yuz,"-->",tekrar_say[yuz])