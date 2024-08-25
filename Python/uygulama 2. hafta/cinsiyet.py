#cinsiyetin belirtilmesi için girilen karakterin doğru (e/E/k/K) olup olmadığını bulan kod
cins = input("Cinsiyetinizi giriniz : ")

if  cins == 'e' or 'E' or 'k' or 'K' :
    print("Doğru")
else :
    print("Hatalı")

#if not cins== şeklinde gitseydi hatalı yazısı çıkardı
#or'lar and'e dönüşürse de hatalı yazısı çıkardı
#if cins in ['e','E','k','K'] diye de gösterilebilir (listeleme)