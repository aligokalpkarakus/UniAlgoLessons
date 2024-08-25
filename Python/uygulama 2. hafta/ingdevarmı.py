#girilen bir karakterin ingilizce'De yer alan bir karakter olup olmadığının kodu:
karakter = input("Bir karakter giriniz : ")

if karakter >= 'A' and karakter <= 'Z' or karakter >= 'a' and karakter <= 'z' :
    print("İngilizce'de var.")
else :
    print("İngilizce'de yok.")

#aynı zamanda 'A' <= karakter <= 'Z' ve 'a' <= karakter <= 'z' şeklinde yazılabilir