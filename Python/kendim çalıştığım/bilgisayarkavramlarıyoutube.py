#BilgisayarKavramlari adlı youtube kanalından izleyerek aldığım notlar
#matematik işlemleri dümdüz yapılabilir
2+4
2*4
2+4+5+6
2*(3+1) #işlemlerin sonuçlarını çıktı olarak alırız

#rakamları ve sayıları değişken olarak atayabiliriz
x = 10
y = 20
print(x+y) #30 diye çıktı alınır

#xyz yazarsak xyz diye bir değişken daha tanımlanmadığı için hata alırız
xyz = 200
print(xyz) #artık xyz yazarsak değişken atadığımız ve çıktısını istediğimiz için yazdırabiliriz

###
vergi = 18/100
print(vergi) #0.18 diye çıktı alırız
satis = 154.32
print(vergi * satis) #sonucun çıktısını alırız
print(satis +_) #python idle'sında _ bir önceki sonuca tekabül ediyor yani bunun normalde satis + vergi * satis gibi okunup toplama işlemi yapması lazım ama pycharmda hata aldım
round(_,2) # üstteki satis + _ sonucunu _'a atayıp (önceki sonuç anlamında) 2 yazarak virgülden sonraki hane sayısını belirtiriz

#dizgiler (strings)
"merhaba dünya" # 'merhaba dünya' diye çıktısı alınır
x = 'bilgisayar kavramları' # x yazıldığında 'bilgisayar kavramları diye çıktı alınır tırnaklar gitmez çünkü o da değişken olarak sayılır
print(x) #çıktısında bilgisayar kavramları yazar tırnaklar olmaz çünkü print komutu tırnak içini okur tırnağı okumaz

x = 'bilgisayar \nkavramlari' #çıktısı bilgisayar \n kavramlari şeklinde olur \n aslında kendisinden sonraki karakterleri alt satıra gönderir ama değişkene atandığı için okunmaz
print(x) #çıktısında ilk satıra bilgisayar 2. satıra kavramlari yazdırılır çünkü print komutu tırnağın içini okur ve komutları uygular yani \n değerlendirilir

y = "ali'nin evi" #y değişkenini direkt "ali'nin evi" olarak çıkar tırnaklarda problem yoktur
y = 'ali'nin evi # evinden sonra da ' gelecek ama program izin vermiyor. bunun çıktısı alınamaz çünkü tırnaklar hatalı
z = 'ali\'nin evi' # şeklinde yazıldığında \ özel karakteri belirtir yani tırnağın kesme işareti olduğunu gösterir 'ali'nin evi' diye çıktı verir
z = "ali \\ xyz " #çıktısı ali \ xyz şeklinde olur çünkü back slash diğer back slashın özel karakter olduğunu gösterir

x+y # yazdığımızda 'bilgisayar \nkavramlariali'nin evi diye çıktı alırız
3*x # 'bilgisayar \nkavramlaribilgisayar \nkavramlaribilgisayar \nkavramlari' diye çıktı verir
3*x+y # 'bilgisayar \nkavramlaribilgisayar \nkavramlaribilgisayar \nkavramlariali'nin evi' diye çıktı verir

x[2] #'l' diye çıktı verir çünkü x değişkeni bilgisayar \nkavramlari demektir [2] demek ise baştan 2. karakteri yazdırır bilgisayar saymaya 0'dan başladığı için l harfi 3. karakter gibi gözükse de bilgisayar 2 olarak okur
x[-2] # değişkenin karakterini sondan sayar yani bilgisayar \nkavramlari derken i -1, r ise -2dir. sondan başlarken 0dan başlamaz 0 en baştaki karaktere ait tekrar etmez
x[2:7] # 2. ve 7. karakterlere kadar yazdırır 'bilgisayar \nkavramlari' yani bu değişkeni 'lgisa' olarak yazdırır
x[2:-2] # baştan 3. ve sondan 2. karakterler arasında kalanları yazdırır yani çıktısı 'lgisayar \nkavramla' olur
x[2:] #baştan 3. karakterden sona kadar çıktısını verir yani 'bilgisayar \nkavramlari' bu değişkeni 'lgisayar \nkavramlari' olarak çıkartır
x[:6] #0'dan 6'ya kadar yazdırır yani 'bilgisayar \nkavramlari' değişkenini 'bilgis' olarak verir

len(x) # bize kaç karakter olduğunu iletir yani 'bilgisayar \nkavramlari' 22 karakterden oluşur. aslında 2 kelimenin toplam harf sayısı 20 ancak bir boşluk karakteri ve n harfi de olduğu için 22 sayıyor. \ karakterden sayılmıyor

#listeler
x = [1,2,3,4] #çıktısı [1,2,3,4] olur. Örneğin aynı kişinin birden fazla bilgisini listeleyerek görebiliriz.
maaslar = [1000,2000,3000]
maaslar [2] #çıktısı [3000] olur
maaslar [-2] #çıktısı [2000] olur
maaslar [1:] #çıktısı [2000, 3000] olur
maaslar + x #çıktısı [1000,2000,3000,1,2,3,4] olur
maaslar = maaslar + x #değişken değiştirilir yani x eklenirse
maaslar #çıktısı [1000,2000,3000,1,2,3,4] olur
maaslar.append(100)
maaslar #çıktısı [1000,2000,3000,1,2,3,4,100] olur yani append listeye yeni bir şey eklemeyi sağlar

ll #listeler listesi demek
ll #çıktısı [[1000,2000,3000,1,2,3,4,100],[1,2,3,4]] olur. ilk liste maaslar 2. liste x'e ait
len(ll) # 2 karakter var sayar çünkü maaslar ve x 2 liste anlamına gelir
ll[1] #çıktısı [1,2,3,4] olur çünkü x 1 olarak görülür maaslar 0
len(ll[1]) #çıktısı 4 olur çünkü 1 2 3 4, 4 adet eleman var
ll[1][2] #1. listenin 2. elemanı demek yani 3 çıktısı alırız
ll[0] #çıktısı [1000,2000,3000,1,2,3,4,100] olur
maaslar #çıktısı [1000,2000,3000,1,2,3,4,100] olur
maaslar.append(10) #maaslar listesine 10 değeri de eklendi
maaslar #çıktısı [1000,2000,3000,1,2,3,4,100,10] olur
ll #çıktısı [[1000,2000,3000,1,2,3,4,100,10],[1,2,3,4]]
maaslar[1] = 200 #çıktıda [[1000,200,3000,1,2,3,4,100],[1,2,3,4]] 2000 200'e dönüştü

#if,elif,else
x = int(input("Bir sayi giriniz"))
if x<200:
    print("kucuk")
elif x>500:
    print("buyuk")
else :
    print("arada")

x = int(input("Bir sayi giriniz"))
if x<200:
    print("kucuk")
    x = 500
elif x>500:
    print("buyuk")
else :
    print("arada")
print("x'in yeni değeri" + str(x)) #çıktı inputa 100 girilirse x = 500 olur ve xin yeni değeri 500 yazdırır stringe çevrilir.

#döngüler while
i = 1
while i < 10:
    print(i)
    i = i+1 #i'yi 1 arttır ve i'ye koy
print("bitti") # çıktısı 1 2 3 4 5 6 7 8 9 bitti olarak olur
#eğer i = i+1 yazmasaydık sonsuza kadar 1 yazardı çünkü şartımıza yani 10'a ulaştıran fonksiyonun yokluğu sayıyı arttıramaz

#fibonacci serisi 0,1,1,2,3,5,8,13..
#                 a,b
#                     c c
#                   a,b
a,b = 0,1
while a<22:
    print(a)
    c = a+b
    a=b
    b=c #önce b'nin içine a'yı koyup byi cnin içine koymalıyız
#2.yol
a,b = 0,1
while a<22:
    print(a)
    a,b=b,a+b #a b oluyor b a+b oluyor

#for döngüsü range ve listelerle kullanılır
l1 = [1,2,39,5,3]
for i in l1:
    print(i) #çıktısı 1 2 39 5 3 i değişkeni listeyi döner

l1 = [1,2,39,5,3]
for i in l1:
    toplam = toplam + i
    print(i)
print(toplam) #kümülatif olarak gider yani i değişkeni başta 1 olur diğer döngüde 2 ile toplanır toplam 3 olur 39 olur ve toplam 42 olur 5 olur ve toplam 47 olur 3 olur ve toplam 50 olur çıktısı 1 2 39 5 3 50 olur

for x in range(5):
    print(x) #çıktısı 0 1 2 3 4 olur

l2 = range(5)
prin(l2) #çıktısı #[1,2,3,4] olur

l2 = range(2,15,2) #2den 15e kadar ikişer ikişer arttır demek çıktısı [2,4,6,8,10,12,14] olur
prin(l2)

l2 = range(15,2,-2) #15ten 2ye ikişer azalarak git çıktısı [15,13,11,9,7,5,3] olur
print(l2)

#continue break döngüleri
for x in range(1,20):
    if(x%3==00):
        continue
    print(x) #çıktısı 1 2 4 5 7 8..20 üçe bölünenleri yazdırmadı x 1 iken direkt printler continue aktive olmaz ama 3e geldiğinde üçe bölünebilirliği sorgulanır bölündüğü için continue aktif olur ve printlemez

for x in range(1,20):
    if(x%3==00):
        break
    print(x) #break durdurma anlamı taşır kod çalıştığında çıktısı 1 2 olur 3 3e bölündüğü için break aktif olur ve sayı yazmak durur

#pass
while True:
    pass #boş demek yani hiçbir şey yapılmayacak

#birden yüze kadar olan asal sayıları yazdırma ödevi

for n in range(2,10):
    for x in range(1,n)
        if n % x == 0:
            print(n, "equals", x, '*', n//x)

for i in range(1:100):
    bolunurmu = False;
        for b in range(2:i):
            if(i%b==0):
                bolunurmu = True
        if(flag):
            print(i)

sonuc = []
for i in range(1, 100):
    for b in range(2, i):
        if i % b == 0:
            break
    else:
        sonuc.append(i)
print(sonuc)


#fonksiyonlar
def f(x):
    return x+10 #x parametresini onla topla geri döndür
print(f(8)) #printin içine 18 yazılmış gibi çıktı alıcaz çıktı 18 olur

def merhaba():
    print("merhabe dünya")
merhaba() #bu fonksiyon istenen fonksiyonu icra edecek ve merhaba dünya yazdıracak

def merhaba(parametre):
    print("merhabe"+parametre)
merhaba(gökalp) # merhaba gökalp diye çıktı alırız

merhaba(10) # çıktısı hata verir çünkü integer ve string toplanmaya çalışır.

def merhaba():
    if(type(parametre)==int):
        print("merhaba"+str(parametre)) # stringe çevir ve öyle topla demek str()
    else:
        print("merhaba"+parametre)
merhaba(10) # bu sefer çıktı verir

def fib(n):
    a,b = 0,1
    while a < n:
        print(a)
        a,  b = b, b+a
fib(20) #çıktısı fibonaccidir 0 1 1 2 3 5 8 13

#özyineli fonksiyon
def fact(n):
    a = 1
    sonuc = 1
    while a<=n:
        sonuc = sonuc*a
        a = a+1
    return sonuc #sonucun hesaplandığını ve döndürüldüğünü belirtmek için
print(fact(5)) # çıktısı 120 olur

# n! = n * (n-1)!

def facto(n):
    if n == 0:
        return 1 # aşağıdaki problemi bu şekilde çözeriz. n 0 olduğunda return geri dönderecek
    return n * facto(n*1) #faktöriyel fonksiyonunu n çarpı n-1 ile tanımlıyoruz. bir problemi var o da sonsuza gidişi
print(facto(5)) # çıktısı 120 olur. 120 yi bulana kadar şunları yapar : 5 * 4! snra 4 * 3! sonra 3 * 2! sonra 2 * ! sonra 1 * 0! bire gelince if çalışacak ve faktöriyele son verecek

#özyineli fonksiyon ile fibonacci
#0,1,1,2,3,5,8,13
#0,1,2,3,4,5,6,7
#fibo(7) = fibo (6) + fibo(5)    13 = 8 + 5
def fibo(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibo(n-1) + fibo(n-2)
print(fibo(7)) # çıktısı 13

#g(x,y) = x + 5 * y
def g(x,y)
    return x + 5*y
print(g(2,3)) # 17 yazar

def g(x,y=3)
    return x + 5*y
print(g(2,5)) # 5 girdiğimiz için yukarıda y=3 ün hükmü kalmaz çıktısı 27
print(g(2)) # çıktısı yine 17 çünkü en başta 3 dedik.

# argüman listeleri
def fonk(a):
    print(a)
fonk(10) # ekrana 10 basar

def topla(a,b):
    return a+b
print(topla(2,3)) # 5 basar
print(topla(2,3,4,5)) # 2 parametre alınacak denip 4 parametre girilirse çalışmaz
print(topla(2)) # eksik parametre girişinden çalışmaz

#parametre sayısı uyuşmama probleminin önüne geçmek için
def bastir(*a) # liste şeklinde alacak demek
    print(a) # listeyi basıp liste olduğunu anlayalım
    for i in a: # a liste olarak gelecek
        print(i) # listenin değerlerini yazdırsın
bastir(1,2,3,4,5) # çıkış şekli (1,2,3,4,5) 1 2 3 4 5 şeklinde olur önce listeyi gösterir sonra değerlerini
bastir(1) # çıkış şekli (1) 1 şeklinde olur
bastir(1,2,3) # çıkış şekli (1,2,3) 1 2 3 şeklinde olur

def topla (*a):
    sonuc = 0
    for i in a:
        sonuc = sonuc + i
    return sonuc
print(topla(2,3)) #çıktısı 5
print(topla(2,3,4,5)) # çıktısı 14
print(topla(2)) # çıktısı 2

#parametreyi argüman yapabiliriz
def toplab(baslangic,*a):
    sonuc = baslangic
    print("baslangic"+str(baslangic))
    for i in a:
        sonuc = sonuc + i
    return sonuc
print(toplab(2,3,4,5)) # baslangic : 2 14 diye çıktı verir, ilk değer baslangıca return olur  3 4 5 argüman listesine girmiş

#keywordler
def fonksiyon(**a):
    for i in a:
        print(str(i + a[i]))
fonksiyon(a=2,b=3,c=4) #çıktısı a2 c4 b3 diye çıktı verir