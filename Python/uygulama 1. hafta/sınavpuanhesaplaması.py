LAB_KATSAYISI=0.2
ARASINAV_KATSAYISI=0.3
FINAL_KATSAYISI=0.5

ogrenci_no = input("Öğrenci numaranızı giriniz = ")
ad_soyad = input("Adınızı soyadınızı giriniz = ")
lab_notu = int(input("Lab notunuzu giriniz = "))
arasinav_notu = int(input("Arasınav notunuzu giriniz = "))
final_notu = int(input("Final notunuzu giriniz = "))

donem_sonu_notu = lab_notu * LAB_KATSAYISI + arasinav_notu * ARASINAV_KATSAYISI + final_notu * FINAL_KATSAYISI

print(f'Sayın {ogrenci_no}' + f' numaralı {ad_soyad};')
print(f'Lab notunuz = {lab_notu}')
print(f'Arasınav notunuz = {arasinav_notu}')
print(f'Final notunuz = {final_notu}')
print(f'Dönem sonu notunuz = {donem_sonu_notu}')