n = int(input())
d = int(input())
l = []
res = 0
for i in range(n-1):
    l.append(int(input()))

l.sort(reverse = True)

if n == 1 :
    print(0)

else:
    while l[0] >= d:
        d += 1
        l[0] -= 1
        res += 1
        l.sort(reverse=True)

    print(res)

