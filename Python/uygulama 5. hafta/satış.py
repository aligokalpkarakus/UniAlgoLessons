yil_top = 0
ay_top_max = -1

for ay_no in range(1,13):
    ay_top = 0
    for gun_no in range(1,31):
        gun_satis = int(input(f"{ay_no}. ayda {gun_no}. gününün satış adedini giriniz:"))
        ay_top += gun_satis
        yil_top += ay_top
    print(ay_no,". ayın satış toplamı:",ay_top)

    if ay_top > ay_top_max:
        ay_top_max = ay_top
        ay_top_max_ay_no = ay_no

print(f"Yıllık satış adedi: {yil_top}")
print(f"En çok satış {ay_top_max_ay_no}. ay, {ay_top} adet.")