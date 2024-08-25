a = int(input("Bir sayı giriniz : "))
b = int(input("Bir sayı giriniz : "))
c = int(input("Bir sayı giriniz : "))

if b < a < c or c < a < b :
    print("A sayısı c ve b sayılarının arasında.")
else :
    print("A sayısı c ve b sayılarının arasında değil.")

if a == b and a < c :
    print("A sayısı b sayısına eşit ve c sayısından küçük.")
else :
    print("A sayısı b sayısına eşit ama c sayısından küçük")

if a > b or a > c :
    print("A sayısı b veya c'den büyük")