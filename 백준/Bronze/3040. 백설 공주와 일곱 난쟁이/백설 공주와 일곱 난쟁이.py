l = []
for i in range(9) :
    a = int(input())
    l.append(a)

for j in range(8):
    for k in range(j+1, 9) :
        if sum(l) - l[j]-l[k] == 100 :
            x, y = j, k
            break

l.pop(x)
l.pop(y-1)
for i in l :
    print(i)