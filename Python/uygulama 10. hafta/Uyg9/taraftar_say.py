#Problem:
# Bir topluluktaki kişilerin taraftarı oldukları futbol takımının adını (büyük harflerle) alan,
# her kişiden sonra başka kişi olup olmadığını soran (e/h) ve girilen takım adlarını ve bu
# takımların taraftar sayılarını ekranda listeleyen bir algoritma ve program yazınız.


#Algoritma:
#def verileri_al_ve_taratar_sayilarini_hesapla(takim_taraftar_say):
#    devam='e'
#    while devam=='e':
#        takim=input()
#
#        if takim in takim_taraftar_say:
#            takim_taraftar_say[takim]+=1
#        else:
#            takim_taraftar_say[takim]=1
#
#        devam=input()
#
#def taraftar_sayilarini_yazdir(takim_taraftar_say):
#    for takim in takim_taraftar_say:
#        print(takim,takim_taraftar_say[takim])
#
#def main():
#    takim_taraftar_say = {}
#    verileri_al_ve_taratar_sayilarini_hesapla(takim_taraftar_say)
#    taraftar_sayilarini_yazdir(takim_taraftar_say)
#
#main()


#Program:
def verileri_al_ve_taratar_sayilarini_hesapla(takim_taraftar_say):
    devam='e'
    while devam=='e':
        takim=input("Taraftari oldugunuz takimin kisa adini giriniz:")

        # Alternatif-1
        # if takim in takim_taraftar_say:
        #     takim_taraftar_say[takim]+=1
        # else:
        #     takim_taraftar_say[takim]=1

        # Alternatif-2
        # try:
        #     takim_taraftar_say[takim] += 1
        # except KeyError:
        #     takim_taraftar_say[takim] = 1

        # Alternatif-3
        takim_taraftar_say[takim]=takim_taraftar_say.get(takim,0)+1

        devam=input("Baska taraftar var mi?")

def taraftar_sayilarini_yazdir(takim_taraftar_say):
    # Alternatif-1
    # for takim in takim_taraftar_say:
    #     print(takim,takim_taraftar_say[takim])

    #Alternatif-2
    for takim,taraftar_say in takim_taraftar_say.items():
        print(takim,taraftar_say)

def main():
    takim_taraftar_say = {}
    verileri_al_ve_taratar_sayilarini_hesapla(takim_taraftar_say)
    taraftar_sayilarini_yazdir(takim_taraftar_say)

main()
