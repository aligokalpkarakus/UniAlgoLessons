#Problem:
# Birim saat ücreti 53,45 TL olan bir işçinin, bir haftada kaç saat
# çalıştığını (tamsayı) alan ve o hafta işçiye ödenecek haftalık ücreti
# hesaplayarak ekrana yazdıran bir algoritma ve program yazınız.
# Haftalık normal çalışma süresi 40 saattir ve bu süreyi aşan saatler
# için birim saat ücretinin 1,5 katı ödeme yapılmaktadır.


#Algoritma:
#BIRIM_UCRET=53.45 #named constant(isimlendirilmis sabit)
#HAFTALIK_NORMAL_SURE=40 #named constant(isimlendirilmis sabit)
#FAZLA_MESAI_ORANI=1.5 #named constant(isimlendirilmis sabit)
#
#calisma_suresi=input()
#
#if calisma_suresi<=HAFTALIK_NORMAL_SURE:
#    ucret=calisma_suresi*BIRIM_UCRET
#else:
#    ucret=HAFTALIK_NORMAL_SURE*BIRIM_UCRET+(calisma_suresi-HAFTALIK_NORMAL_SURE)*BIRIM_UCRET*FAZLA_MESAI_ORANI
#
#print(ucret)


#Program:
BIRIM_UCRET=53.45 #named constant(isimlendirilmis sabit)
HAFTALIK_NORMAL_SURE=40 #named constant(isimlendirilmis sabit)
FAZLA_MESAI_ORANI=1.5 #named constant(isimlendirilmis sabit)

calisma_suresi=int(input("haftalik calistiginiz sureyi (tamsayı) giriniz:"))

if calisma_suresi<=HAFTALIK_NORMAL_SURE:
    ucret=calisma_suresi*BIRIM_UCRET
else:
    ucret=HAFTALIK_NORMAL_SURE*BIRIM_UCRET+(calisma_suresi-HAFTALIK_NORMAL_SURE)*BIRIM_UCRET*FAZLA_MESAI_ORANI

print(f"haftalık alacaginiz ucret: {ucret:.2f} TL")
