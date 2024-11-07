n, m = map(int,input().split())
dic = {}

for a in range (1,n+1) :
    dic[a] = 0


for b in range (1,m+1) :
    i, j, k = map(int,input().split())

    for c in range(i, j+1) :
        dic[c] = k
        c += 1
    
    b += 1

for d in range(1, n+1) :
    print(dic[d], end=' ')