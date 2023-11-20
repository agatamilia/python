import itertools 
a=int(input())
b = range(a)
x = int(input())
komb = itertools.combinations(b,x) 
print(len(list(komb)))