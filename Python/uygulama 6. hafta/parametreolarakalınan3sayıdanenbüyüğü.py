# parametre olarak alınan 3 sayının en büyüğü
def sayilar(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        max = num1
    elif num2 > num3:
        max = num2
    else:
        max = num3
    return max

num1 = int(input("sayi1:"))
num2 = int(input("sayi2:"))
num3 = int(input("sayi3:"))

print(sayilar(num1,num2,num3))
