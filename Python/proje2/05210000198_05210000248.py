def karakter_secimi(sutun, kaca_kac, satir):
    global birinci_oyuncu, ikinci_oyuncu
    hata1 = 'e'
    hata2 = 'e'
    birinci_oyuncu = input("1. oyuncuyu temsil etmek için karakter giriniz:")  # birinci oyuncunun girişi ve kontrolleri
    while hata1 == 'e':
        if len(birinci_oyuncu) > 1 or len(birinci_oyuncu) == 0:
            birinci_oyuncu = input("1. oyuncuyu temsil etmek için bir karakter giriniz:")
            hata1 = 'e'
        elif birinci_oyuncu == " ":
            birinci_oyuncu = input("1. oyuncuyu temsil etmek için boşluk karakterinden başka karakter giriniz:")
            hata1 = 'e'
        else:
            hata1 = 'h'
    ikinci_oyuncu = input("2. oyuncuyu temsil etmek için karakter giriniz:")  # ikinci oyunun girişi ve kontrolleri
    while hata2 == 'e':
        if len(ikinci_oyuncu) > 1 or len(ikinci_oyuncu) == 0:
            ikinci_oyuncu = input("2. oyuncuyu temsil etmek için bir karakter giriniz:")
            hata2 = 'e'
        elif ikinci_oyuncu == " ":
            ikinci_oyuncu = input("2. oyuncuyu temsil etmek için boşluk karakterinden başka karakter giriniz:")
            hata2 = 'e'
        elif birinci_oyuncu == ikinci_oyuncu:
            print("Oyuncu taşları aynı olamaz.")
            ikinci_oyuncu = input("2. oyuncuyu temsil etmek için bir karakter giriniz:")
            hata2 = 'e'
        else:
            hata2 = 'h'
    if hata1 == 'h' and hata2 == 'h':  # kullanıcı girişleri hatasızsa
        birinci_oyuncu = birinci_oyuncu.upper()
        ikinci_oyuncu = ikinci_oyuncu.upper()
        print(f"Birinci oyuncunun seçtiği karakter: {birinci_oyuncu}")
        print(f"İkinci oyuncunun seçtiği karakter: {ikinci_oyuncu}")
    for index in range(kaca_kac):  # ilk ve son satırlara karakterleri yazdırma
        sutun[kaca_kac - 1][index] = birinci_oyuncu
        sutun[0][index] = ikinci_oyuncu
    print()
    tablo(kaca_kac, sutun, satir)
    print()


def hareketlendirme(sutun, kaca_kac, satir, kalan_1, kalan_2):
    oyuncu = 2
    global birinci_oyuncu, ikinci_oyuncu, hamle_yapan
    while True:
        try:
            while kalan_1 > 1 and kalan_2 > 1:  # kalan taş sayısına göre bitiş
                hatasiz_hamle = 'e'
                if oyuncu % 2 == 0:  # çift veya tek sayı olmasına göre hamle yaptırma
                    hamle_yapan = birinci_oyuncu
                    bekleyen = ikinci_oyuncu
                else:
                    hamle_yapan = ikinci_oyuncu
                    bekleyen = birinci_oyuncu
                print()
                konum_degisim = input(
                    f"Oyuncu {hamle_yapan}, lütfen hareket ettirmek istediğiniz kendi taşınızın konumunu ve hedef "
                    f"konumunu giriniz (ör:1A 2A):")  # gidilecek konum için giriş
                while len(konum_degisim) > 5 or len(konum_degisim) < 5:  # 5 karaktere ihtiyaç olduğundan kontrol
                    konum_degisim = input(
                        f"Oyuncu {hamle_yapan}, hatalı giriş. Lütfen hareket ettirmek istediğiniz kendi taşınızın "
                        f"konumunu ve hedef konumunu tekrar giriniz (ör:1A 2A):")
                hedef_liste = list(konum_degisim)  # girilen veriyi listeye dönüştürme
                hedef_liste[1] = hedef_liste[1].upper()  # hareket ettirmede küçük harf girilmesine karşın önlem
                hedef_liste[4] = hedef_liste[4].upper()
                print()
                while hatasiz_hamle == 'e':  # hamle hatalarının kontrolü
                    if sutun[int(hedef_liste[0]) - 1][satir.index(str(hedef_liste[1]))] == " ":
                        print("Belirtmiş olduğunuz ilk konumda taşınız yok.")
                        hatasiz_hamle = 'e'
                    elif hedef_liste[2] != " ":
                        print("Boşluk karakteri olacak şekilde örneğin 1A 5A olarak giriniz.")
                        hatasiz_hamle = 'e'
                    elif hedef_liste[1] != hedef_liste[4] and hedef_liste[0] != hedef_liste[3]:
                        print("Lütfen bulunduğunuz satır ve sütun boyunca hareket ettirin.")
                        hatasiz_hamle = 'e'
                    elif sutun[int(hedef_liste[0]) - 1][satir.index(str(hedef_liste[1]))] != hamle_yapan:
                        print("Size ait olmayan bir taşı hareket ettirmeye çalıştınız.")
                        hatasiz_hamle = 'e'
                    elif sutun[int(hedef_liste[3]) - 1][satir.index(str(hedef_liste[4]))] != " ":
                        print("Belirtmiş olduğunuz son konum dolu.")
                        hatasiz_hamle = 'e'
                    else:
                        hatasiz_hamle = 'yok'
                    if hatasiz_hamle == 'e':
                        konum_degisim = input(
                            f"Oyuncu {hamle_yapan}, hatalı giriş. Lütfen hareket ettirmek istediğiniz kendi "
                            f"taşınızın konumunu ve hedef konumunu giriniz:")
                        while len(konum_degisim) > 5 or len(konum_degisim) < 5:
                            konum_degisim = input(
                                f"Oyuncu {hamle_yapan}, hatalı giriş. Lütfen hareket ettirmek istediğiniz "
                                f"kendi taşınızın konumunu ve hedef konumunu tekrar giriniz (ör:1A 2A):")
                        hedef_liste = list(konum_degisim)
                        hedef_liste[1] = hedef_liste[1].upper()
                        hedef_liste[4] = hedef_liste[4].upper()
                        print()
                    while hatasiz_hamle == 'yok':  # üstünden atlamaya engel olmak için yazılan kısım
                        if sutun[int(hedef_liste[0]) - 1] == sutun[int(hedef_liste[3]) - 1] and \
                                satir.index(str(hedef_liste[1])) > satir.index(str(hedef_liste[4])):
                            for i in range(satir.index(str(hedef_liste[4])), satir.index(str(hedef_liste[1]))):
                                if sutun[int(hedef_liste[0]) - 1][i] != " ":
                                    print("Belirtmiş olduğunuz konuma giden yol dolu.")
                                    hatasiz_hamle = 'e'
                                    break
                                else:
                                    hatasiz_hamle = 'yok'
                        elif sutun[int(hedef_liste[0]) - 1] == sutun[int(hedef_liste[3]) - 1] and \
                                satir.index(str(hedef_liste[1])) < satir.index(str(hedef_liste[4])):
                            for i in range(satir.index(str(hedef_liste[1])), satir.index(str(hedef_liste[4]))):
                                if sutun[int(hedef_liste[0]) - 1][i + 1] != " ":
                                    print("Belirtmiş olduğunuz konuma giden yol dolu.")
                                    hatasiz_hamle = 'e'
                                    break
                                else:
                                    hatasiz_hamle = 'yok'
                        elif satir.index(str(hedef_liste[1])) == satir.index(str(hedef_liste[4])) and \
                                int(hedef_liste[0]) < int(hedef_liste[3]):
                            for i in range(int(hedef_liste[0]) - 1, int(hedef_liste[3]) - 1):
                                if sutun[i + 1][satir.index(str(hedef_liste[1]))] != " ":
                                    print("Belirtmiş olduğunuz konuma giden yol dolu.")
                                    hatasiz_hamle = 'e'
                                    break
                                else:
                                    hatasiz_hamle = 'yok'
                        elif satir.index(str(hedef_liste[1])) == satir.index(str(hedef_liste[4])) and \
                                int(hedef_liste[0]) > int(hedef_liste[3]):
                            for i in range(int(hedef_liste[3]), int(hedef_liste[0])):
                                if sutun[i - 1][satir.index(str(hedef_liste[1]))] != " ":
                                    print("Belirtmiş olduğunuz konuma giden yol dolu.")
                                    hatasiz_hamle = 'e'
                                    break
                                else:
                                    hatasiz_hamle = 'yok'
                        else:
                            break
                        if hatasiz_hamle == 'e':
                            konum_degisim = input(
                                f"Oyuncu {hamle_yapan}, lütfen hareket ettirmek istediğiniz kendi "
                                f"taşınızın konumunu ve hedef konumunu giriniz:")
                            while len(konum_degisim) > 5 or len(konum_degisim) < 5:
                                konum_degisim = input(
                                    f"Oyuncu {hamle_yapan}, hatalı giriş. Lütfen hareket ettirmek istediğiniz "
                                    f"kendi taşınızın konumunu ve hedef konumunu tekrar giriniz (ör:1A 2A):")
                            hedef_liste = list(konum_degisim)
                            hedef_liste[1] = hedef_liste[1].upper()
                            hedef_liste[4] = hedef_liste[4].upper()
                            print()
                        else:
                            break
                while hatasiz_hamle == 'yok':  # eğer hata yoksa harekete ettirme kısmı
                    sutun[int(hedef_liste[0]) - 1][satir.index(str(hedef_liste[1]))] = " "
                    sutun[int(hedef_liste[3]) - 1][satir.index(str(hedef_liste[4]))] = hamle_yapan
                    if kaca_kac - 1 >= int(hedef_liste[3]) + 1:  # sütundaki kıstırma kontrolü
                        if sutun[int(hedef_liste[3]) - 1][satir.index(str(hedef_liste[4]))] == \
                                sutun[int(hedef_liste[3]) + 1][satir.index(str(hedef_liste[4]))] == \
                                hamle_yapan and sutun[int(hedef_liste[3])][
                                satir.index(str(hedef_liste[4]))] == bekleyen:
                            sutun[int(hedef_liste[3])][satir.index(str(hedef_liste[4]))] = " "
                            print(f"{bekleyen} taşı {int(hedef_liste[3]) + 1}{hedef_liste[4]} konumundan çıkarıldı.")
                            if hamle_yapan == birinci_oyuncu:
                                kalan_2 -= 1
                            else:
                                kalan_1 -= 1

                    if int(hedef_liste[3]) - 3 >= 0:  # sütundaki kıstırma kontrolü
                        if sutun[int(hedef_liste[3]) - 1][satir.index(str(hedef_liste[4]))] == \
                                sutun[int(hedef_liste[3]) - 3][
                                    satir.index(str(hedef_liste[4]))] == hamle_yapan and sutun[int(hedef_liste[3]) - 2][
                                satir.index(str(hedef_liste[4]))] == bekleyen:
                            sutun[int(hedef_liste[3]) - 2][satir.index(str(hedef_liste[4]))] = " "
                            print(f"{bekleyen} taşı {int(hedef_liste[3]) - 1}{hedef_liste[4]} konumundan çıkarıldı.")
                            if hamle_yapan == birinci_oyuncu:
                                kalan_2 -= 1
                            else:
                                kalan_1 -= 1

                    if kaca_kac - 1 >= satir.index(str(hedef_liste[4])) + 2:  # satırdaki kıstırma kontrolü
                        if sutun[int(hedef_liste[3]) - 1][satir.index(str(hedef_liste[4]))] == \
                                sutun[int(hedef_liste[3]) - 1][
                                    satir.index(str(hedef_liste[4])) + 2] == hamle_yapan and \
                                sutun[int(hedef_liste[3]) - 1][
                                    satir.index(str(hedef_liste[4])) + 1] == bekleyen:
                            sutun[int(hedef_liste[3]) - 1][satir.index(str(hedef_liste[4])) + 1] = " "
                            print(f"{bekleyen} taşı {int(hedef_liste[3])}"
                                  f"{satir[satir.index(str(hedef_liste[4])) + 1]} konumundan çıkarıldı.")
                            if hamle_yapan == birinci_oyuncu:
                                kalan_2 -= 1
                            else:
                                kalan_1 -= 1

                    if satir.index(str(hedef_liste[4])) - 2 >= 0:  # satırdaki kıstırma kontrolü
                        if sutun[int(hedef_liste[3]) - 1][satir.index(str(hedef_liste[4]))] == \
                                sutun[int(hedef_liste[3]) - 1][
                                    satir.index(str(hedef_liste[4])) - 2] == hamle_yapan and \
                                sutun[int(hedef_liste[3]) - 1][
                                    satir.index(str(hedef_liste[4])) - 1] == bekleyen:
                            sutun[int(hedef_liste[3]) - 1][satir.index(str(hedef_liste[4])) - 1] = " "
                            print(f"{bekleyen} taşı {int(hedef_liste[3])}"
                                  f"{satir[satir.index(str(hedef_liste[4])) - 1]} konumundan çıkarıldı.")
                            if hamle_yapan == birinci_oyuncu:
                                kalan_2 -= 1
                            else:
                                kalan_1 -= 1

                    if sutun[0][0] == bekleyen and sutun[0][1] == hamle_yapan and sutun[1][0] == hamle_yapan:
                        # sol üst köşedeki kıstırma
                        sutun[0][0] = " "
                        print(f"{bekleyen} taşı 1A konumundan çıkarıldı")
                        if hamle_yapan == birinci_oyuncu:
                            kalan_2 -= 1
                        else:
                            kalan_1 -= 1

                    elif sutun[kaca_kac - 1][0] == bekleyen and sutun[kaca_kac - 2][0] == \
                            hamle_yapan and sutun[kaca_kac - 1][1] == hamle_yapan:  # sol alt köşedeki kıstırma
                        sutun[kaca_kac - 1][0] = " "
                        print(f"{bekleyen} taşı {kaca_kac}A konumundan çıkarıldı.")
                        if hamle_yapan == birinci_oyuncu:
                            kalan_2 -= 1
                        else:
                            kalan_1 -= 1

                    elif sutun[0][kaca_kac - 1] == bekleyen and \
                            sutun[0][kaca_kac - 2] == hamle_yapan and \
                            sutun[1][kaca_kac - 1] == hamle_yapan:  # sağ üst köşedeki kıstırma
                        sutun[0][kaca_kac - 1] = " "
                        print(f"{bekleyen} taşı 1{satir[kaca_kac - 1]} konumundan çıkarıldı.")
                        if hamle_yapan == birinci_oyuncu:
                            kalan_2 -= 1
                        else:
                            kalan_1 -= 1

                    elif sutun[kaca_kac - 1][kaca_kac - 1] == bekleyen and \
                            sutun[kaca_kac - 1][kaca_kac - 2] == hamle_yapan and \
                            sutun[kaca_kac - 2][kaca_kac - 1] == hamle_yapan:  # sağ alt köşedeki kıstırma
                        sutun[kaca_kac - 1][kaca_kac - 1] = " "
                        print(f"{bekleyen} taşı {kaca_kac}{satir[kaca_kac - 1]} konumundan çıkarıldı.")
                        if hamle_yapan == birinci_oyuncu:
                            kalan_2 -= 1
                        else:
                            kalan_1 -= 1
                    tablo(kaca_kac, sutun, satir)
                    print()
                    oyuncu += 1  # tek çift sayı kontrolü için
                    break
            print()
            if kalan_1 > kalan_2:  # son hamle yapan oyunu kazanacağı için kazananı gösterme
                print(f"Oyuncu {hamle_yapan} oyunu kazandı.")
            else:
                print(f"Oyuncu {hamle_yapan} oyunu kazandı.")
            print("Oyun bitti..")
            print()
            break

        except IndexError:
            print("Index hatası. Oyun alanının dışında yer seçildi.")
        except ValueError:
            print("Hatalı giriş tekrar giriniz (ör:1A 3A).")


def tablo(kaca_kac, sutun, satir):
    for x in range(kaca_kac):  # üste harfleri yazdırma
        print("   ", end="")
        print(f"{satir[x]}", end="")
    print("")
    print(" -", end="")
    print("----" * kaca_kac)
    for y in range(kaca_kac):  # çift boyutlu listeyi yazdırma
        print(f"{y + 1}| ", end="")
        for sayi in range(kaca_kac):
            print(f"{sutun[y][sayi]}", end=" | ")
        print(f"{y + 1}")
        print(" -", end="")
        print("----" * kaca_kac)
    for x in range(kaca_kac):  # alta harfleri yazdırma
        print("   ", end="")
        print(f"{satir[x]}", end="")


def main():
    print("    KİLİT OYUNUNA HOŞ GELDİNİZ")
    print("    --------------------------")
    MIN_TABLO = 4
    MAX_TABLO = 8
    devam = 'e'
    while devam == 'e' or devam == 'E':
        try:
            kaca_kac = int(input("Oyun alanının satır/sütun sayısını giriniz(4-8):"))
            while not MIN_TABLO <= kaca_kac <= MAX_TABLO:
                kaca_kac = int(input("Oyun alanının satır/sütun tekrar sayısını giriniz(4-8):"))
            satir = ["A", "B", "C", "D", "E", "F", "G", "H"]
            sutun = [[" " for a in range(kaca_kac)] for b in range(kaca_kac)]
            kalan_1 = kaca_kac
            kalan_2 = kaca_kac
            karakter_secimi(sutun, kaca_kac, satir)
            hareketlendirme(sutun, kaca_kac, satir, kalan_1, kalan_2)
            devam = input("Tekrar oynamak istiyor musunuz? (e/E/h/H):")
            while devam not in ['e', 'E', 'h', 'H']:
                print("Hatalı giriş, lütfen e/E/h/H karakterlerden birini giriniz.")
                devam = input("Tekrar oynamak istiyor musunuz? (e/E/h/H):")
            if devam in ['h', 'H']:
                print("Oynadığınız için teşekkür eder yine bekleriz...")
        except ValueError:
            print("Integer yani sayı girilmeli.")


main()
