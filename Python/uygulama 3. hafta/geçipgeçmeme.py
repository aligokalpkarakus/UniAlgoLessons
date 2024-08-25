# Bir dersin iki arasınavının ortalaması en az 75 ise finalden muaf olarak, değilse arasınav ortalamasının %40ı ile finalin %60ının toplamı en az 50 ise ders geçiliyor algoritması:

FINAL_MUAF = 75
ARASINAV_KATSAYI = 0.4
FINAL_KATSAYI = 0.6
GECME_NOTU = 50

ara1 = int(input("İlk arasınav notunuzu giriniz : "))
ara2 = int(input("İkinci arasınv notunuzu giriniz : "))

ara_ort = (ara1 + ara2) / 2

if ara_ort >= 75:
    print("Finalden muaf olarak dersi geçtiniz.")
else:
    final = int(input("Final notunuzu giriniz : "))
    if (ara_ort * ARASINAV_KATSAYI + final * FINAL_KATSAYI) >= GECME_NOTU:
        print("Finalle beraber geçtiniz.")
    else:
        print("Dersi geçemediniz.")
