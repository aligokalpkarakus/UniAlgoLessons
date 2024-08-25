BIRIM_UCRET = 53.45
HAFTALIK_NORMAL_SURE = 40
FAZLA_MESAI_ORANI = 1.5

calisilan_sure = int(input("Çalışılan süreyi giriniz : "))
if calisilan_sure <= HAFTALIK_NORMAL_SURE:
    ucret = calisilan_sure * BIRIM_UCRET
else:
    ucret = BIRIM_UCRET * HAFTALIK_NORMAL_SURE +  \
            (calisilan_sure - HAFTALIK_NORMAL_SURE) * BIRIM_UCRET * FAZLA_MESAI_ORANI
print(f"Haftalık alacağınız ücret : {ucret:.2f} TL.")
