# Girilen bir metnin palindrom olup olmadığını kontrol eden algoritma

string = input("Metin giriniz:")

"""if string[:] == string[::-1]:
    print("Palindrom")
else:
    print("Değil")"""

"""ters_string = ""
for kar in string:
    ters_string += kar

if ters_string == string:
    print("palindrom")
else:
    print("değil")"""

"""for i in range(len(string) // 2):
    if string[i] != string[i:-1]:
        print("değil")
        break
    else:
        print("palindrom")"""