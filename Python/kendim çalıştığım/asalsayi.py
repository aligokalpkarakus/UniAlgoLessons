sonuc = []
for i in range(1, 100):
    for b in range(2, i):
        if i % b == 0:
            break
    else:
        sonuc.append(i)
print(sonuc)