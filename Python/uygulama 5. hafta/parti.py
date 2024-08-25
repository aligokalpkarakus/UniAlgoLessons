genel_mv_A = 0
genel_mv_B = 0
genel_mv_C = 0

for il_no in range(1,82):
    kont = int(input("Kontenjanı giriniz:"))
    oy_A = int(input("A partisi oy sayısı:"))
    oy_B = int(input("B partisi oy sayısı:"))
    oy_C = int(input("C partisi oy sayısı:"))
    mv_A = 0
    mv_B = 0
    mv_C = 0

    for kont_no in range(1,kont + 1):
        if oy_A > oy_B and oy_A > oy_C:
            mv_A += 1
            oy_A /= 2
        elif oy_B > oy_C:
            mv_B += 1
            oy_B /= 2
        else:
            mv_C += 1
            oy_C /= 2
    print(f"A partisinden MV sayısı: {mv_A}\nB partisinden MV sayısı: {mv_B}\nC partisinden MV sayısı: {mv_C}")
    genel_mv_A += mv_A
    genel_mv_B += mv_B
    genel_mv_C += mv_C

print(f"Genel MV sayıları\nA: {genel_mv_A}\nB: {genel_mv_B}\nC: {genel_mv_C}")