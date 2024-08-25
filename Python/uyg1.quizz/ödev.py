ogr_no = input("Ögrenci numaranızı giriniz = ")
ad_soyad = input("Adınızı ve soyadınızı giriniz = ")
ilk_ders_haftalik_teorik_ders_saati = float(input("Aldığınız ilk dersin haftalık teorik ders saatini giriniz = "))
ilk_ders_haftalik_uygulama_ders_saati = float(input("Aldığınız ilk dersin haftalık uygulama ders saatini giriniz = "))
ilk_ders_haftalik_akts_kredisi = float(input("Aldığınız ilk dersin haftalık AKTS kredisini giriniz = "))
ilk_ders_donem_sonu_notu = float(input("Aldığınız ilk dersin dönem sonu notunu giriniz = "))
ikinci_ders_haftalik_teorik_ders_saati = float(input("Aldığınız ikinci dersin haftalık teorik ders saatini giriniz = "))
ikinci_ders_haftalik_uygulama_ders_saati = float(input("Aldığınız ikinci dersin haftalık uygulama ders saatini giriniz = "))
ikinci_ders_haftalik_akts_kredisi= float(input("Aldığınız ikinci dersin haftalık AKTS kredisini giriniz = "))
ikinci_ders_donem_sonu_notu = float(input("Aldığınız ikinci dersin dönem sonu notunu giriniz = "))

ilk_ders_yerel_kredi = ilk_ders_haftalik_teorik_ders_saati + ilk_ders_haftalik_uygulama_ders_saati / 2
ikinci_ders_yerel_kredi = ikinci_ders_haftalik_teorik_ders_saati + ikinci_ders_haftalik_uygulama_ders_saati / 2
toplam_yerel_kredi = ilk_ders_haftalik_teorik_ders_saati + ilk_ders_haftalik_uygulama_ders_saati / 2  + ikinci_ders_haftalik_teorik_ders_saati + ikinci_ders_haftalik_uygulama_ders_saati / 2
toplam_akts_kredi = ilk_ders_haftalik_akts_kredisi + ikinci_ders_haftalik_akts_kredisi
yerel_krediye_gore_agno = (ilk_ders_donem_sonu_notu * ilk_ders_yerel_kredi + ikinci_ders_donem_sonu_notu * ikinci_ders_yerel_kredi) / toplam_yerel_kredi
aktsye_gore_agno = (ilk_ders_donem_sonu_notu * ilk_ders_haftalik_akts_kredisi + ikinci_ders_donem_sonu_notu * ikinci_ders_haftalik_akts_kredisi) / toplam_akts_kredi

print(f"Ögrenci numarası : {ogr_no}")
print(f"Adı ve soyadı : {ad_soyad}")
print(f"Bu dönem aldığı toplam yerel kredi miktarı : {toplam_yerel_kredi:.2f} ")
print(f"Bu dönem aldığı toplam AKTS kredi miktarı : {toplam_akts_kredi:.2f}")
print(f"Yerel krediye göre bu dönem sonu AGNO : {yerel_krediye_gore_agno:.2f} ")
print(f"AKTS'ye göre bu dönem sonu AGNO : {aktsye_gore_agno:.2f}")