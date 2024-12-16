n = int(input())
a = []
l = 0
cnt_1 = 0
cnt_2 = 0

for i in range(n) :
    q = int(input())
    a.append(q)
    if len(a) == 1 :
        l = q
        cnt_1 += 1

    else :
        if l < q :
            l = q
            cnt_1 += 1

l = 0
for j in range(n-1, -1, -1) :
    if l == 0:
        l = a[-1]
        cnt_2 += 1

    else :
        if l < a[j] :
            l = a[j]
            cnt_2 += 1
        
    

print(cnt_1)
print(cnt_2)