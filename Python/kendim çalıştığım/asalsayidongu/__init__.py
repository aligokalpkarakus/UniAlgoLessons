for n in range(2,100):
    for x in range(1,n):
        if n % x == 0:
            print(n, "equals", x, '*', n//x)

