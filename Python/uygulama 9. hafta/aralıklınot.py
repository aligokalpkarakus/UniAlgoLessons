# bir sınıftaki öğrencilerin notlarını (0-100) kullanıcıdan alan ve 0-9, 10-19,.......,90-100 aralıklarında döndüren
# algoritma

ogr_say = [0] * 10  # 10 öğrenci olsun dedik

devam = 'e'

while devam == 'e':
    for i in range(10):
        bir_not = int(input("Notu giriniz:"))
        while not 0 <= bir_not <= 100:
            bir_not = int(input("Hata. Notu giriniz:"))
        ogr_say[bir_not//10] += 1   # 100 not için bölündüğünde 10 oluyor problemli bura
    devam = input("devam:")

print(ogr_say)