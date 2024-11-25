n = int(input())
h = list(map(int, input().split()))

cnt = 0
a = 0
b = 0

for i in range(len(h)) :
    a = h[i]
    if a>=b :
        cnt +=1
        b = a

    else :
        b = a


print(cnt)