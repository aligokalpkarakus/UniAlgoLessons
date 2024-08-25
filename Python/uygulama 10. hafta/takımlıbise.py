def taraftar_bilgi_al(taraftar_sayilari):
    devam = 'e'
    while devam in ['e', 'E']:
        takim_adi = input("Takım adı:")

        """if takim_adi in taraftar_sayilari:
            taraftar_sayilari[takim_adi] += 1
        else:
            taraftar_sayilari[takim_adi] = 1  """

        """try:
            taraftar_sayilari[takim_adi] += 1
        except KeyError:
            taraftar_sayilari[takim_adi] = 1"""

        taraftar_sayilari[takim_adi] = taraftar_sayilari.get(takim_adi,0) +1


        devam = input("Devam mı:")


def taraftar_sayi_yazdir(taraftar_sayilari):
    for takim_adi in taraftar_sayilari:
        print(f"{takim_adi} = {taraftar_sayilari[takim_adi]}")


def main():
    taraftar_sayilari = {}
    taraftar_bilgi_al(taraftar_sayilari)
    taraftar_sayi_yazdir(taraftar_sayilari)


main()