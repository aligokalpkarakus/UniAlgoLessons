def harf_mi(kar):
    if kar >= 'a' and kar <= 'z' or kar >= 'A' and kar <= 'Z' or kar in ['ğ','Ğ','ü','Ü','i','İ','ö','Ö','ç','Ç']:
        sonuc = True
    else:
        sonuc = False
    return sonuc

harf = input("Harf:")

while harf_mi(harf) == False:
    print("Giriş başarısız.")
    harf = input("Harf:")
else:
    print("Giriş başarılı")
    harf = input("Harf:")