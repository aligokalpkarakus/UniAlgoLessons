# Girilen 2 reel sayıya isteğe göre 4 işlemden birisini uygulayıp sonucu ekrana yazdıran algoritma

sayi1 = int(input("İlk sayıyı giriniz : "))
sayi2 = int(input("İkinci sayıyı giriniz : "))
operator = input("Operatör giriniz : ")

if operator == '+':
    print(sayi1, "+", sayi2, "=", sayi1+sayi2)
elif operator == '-':
    print(sayi1, "-", sayi2, "=", sayi1-sayi2)
elif operator == '*':
    print(sayi1, "*", sayi2, "=", sayi1*sayi2)
elif operator == '/':
    if sayi2 == 0:
        print("0'a bölünme tanımsızdır.")
    else:
        print(sayi1, "/", sayi2, "=", sayi1/sayi2)
else:
    print("Yanlış operatör girildi")