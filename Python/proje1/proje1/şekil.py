def ust_ucgen(ust):
    for satir_no in range(1,ust+1):
        for fonye in range(1,satir_no+1):
            print("♦",end="")
        print()

def alt_ucgen(alt):
    for satir_no in range(alt,0,-1):
        for fonye in range(satir_no-1,0,-1):
            print("♦",end="")
        print()


ust = int(input("a:"))
alt = int(input("b:"))
ust_ucgen(ust)
alt_ucgen(alt)
