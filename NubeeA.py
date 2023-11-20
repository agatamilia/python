x= int (input(''))
rows = int(input(""))
coef = 1

for i in range(x+1, rows+2):
    for space in range(0, rows-i+1):
        print(" ",end="")
    for j in range(0, i):
        if j==0 or i==0:
            coef = 1
        else:
            coef = coef * (i - j)//j
        print(coef, end = " ")
    print()