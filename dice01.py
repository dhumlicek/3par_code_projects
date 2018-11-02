from random import randint

x = 10
n = 0
while n < x:
    r=randint(0,6)
    C='o '
    s='-----\n|'+C[r<1]+' '+C[r<3]+'|\n|'+C[r<5]
    print(s+C[r&1]+s[::-1])
    n += 1