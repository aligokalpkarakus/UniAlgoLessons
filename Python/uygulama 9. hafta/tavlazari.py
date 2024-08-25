# bir tavla zarının 1000 kez atılması sonucunda gelen sayıları kullanıcıdan alan, zarın yüzlerindeki sayıların kaçar kez
# geldiklerini en çok gelen sayıyı ve kaç kez geldiğini bulan algoritma

tekrar_say = [0] * 6  # 6 yüz olduğu için

for atis_no in range(1000):
    yuzey_no = int(input("Yüzey numarasını giriniz:"))
    while yuzey_no < 1 or yuzey_no > 6:
        yuzey_no = int(input("Yüzey numarasını giriniz:"))
    tekrar_say[yuzey_no] += 1

max_tekrar_say_index = 0

for yuzey_no in range(6):
    print(yuzey_no + 1, tekrar_say[yuzey_no])
    if tekrar_say[yuzey_no] > tekrar_say[max_tekrar_say_index]:
        max_tekrar_say_index = yuzey_no
print(max_tekrar_say_index + 1, tekrar_say[max_tekrar_say_index])

