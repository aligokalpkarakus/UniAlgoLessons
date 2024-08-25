#bir dersi geçmek için final ve yıl sonu notunun en az 60 olması gerekmektedir. (yıl sonu notu, iki sınavın ortalamasının %40'ı ile finalin %60'ı toplanarak bulunuyor.) Dersin geçilip geçilmediğinin kodu:
vize1 = int(input("Birinci vize notunuzu giriniz : "))
vize2 = int(input("İkinci vize nbtunuzu giriniz : "))
final = int(input("Final notunuzu giriniz : "))

if  final >= 60 and (vize1 + vize2) / 2 * 0.4 + final * 0.6 >= 60 :
    print("Sınıfı geçtiniz.")
else :
    print("Sınıfı geçemediniz.")