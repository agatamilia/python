i=0
while i!=0:
    i=i-1
else:
    i=i+1
"""

l=[[c for c in range (r)] for r in range (3)]
for x in l:
    for y in x:
        if y<2:
            print('*', end='')
i=0
while i!=0:
    i=i-1
else:
    i=i+1
try:
    print('hello')
    raise Exception
    print(1/0)
except Exception as e:
    print(e)
def f(n):
    if n ==1:
        return 1
    else:
        return n+f (n-1)
print(f(2))
"""