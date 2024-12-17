import math

n = int(input())
l = []

for i in range(n):
    q = int(input())

    if q == 100: 
        l.append(100)
        continue 

    elif q % 10 == 6 or q % 10 == 0:
        q = (q // 10) * 10 + 9

    if q // 10 == 6:
        q = 90 + q % 10

    l.append(q) 

avg = sum(l) / n

if avg-int(avg) >= 0.5 :
    print(math.ceil(avg))
else :
    print(math.floor(avg))