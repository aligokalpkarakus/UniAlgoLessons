ilk_takim_adi = input("İlk takımın adını giriniz : ")
ilk_takim_kazanilan_set = int(input("İlk takımın kazandığı set sayısını giriniz : "))
ikinci_takim_adi = input("İkinci takımnın adını giriniz : ")
ikinci_takim_kazanilan_set = int(input("İkinci takımın kazandığı set sayısını giriniz : "))

if ilk_takim_kazanilan_set > ikinci_takim_kazanilan_set:
    kazanan_takim = ilk_takim_adi
    kaybeden_takim = ikinci_takim_adi
else:
    kazanan_takim = ikinci_takim_adi
    kaybeden_takim = ilk_takim_adi

set_farki = ilk_takim_kazanilan_set - ikinci_takim_kazanilan_set

if -1 <= set_farki <= 1:
    kazanan_takim_puan = 2
    kaybeden_takim_puan = 1
else:
    kazanan_takim_puan = 3
    kaybeden_takim_puan = 0

print(f"Maçı kazanan takımın adı : {kazanan_takim}, kazandığı puan : {kazanan_takim_puan}")
print(f"Maçı kaybeden takımın adı : {kaybeden_takim}, kazandığı puan : {kaybeden_takim_puan}")