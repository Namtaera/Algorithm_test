x = 0

g, w = map(int,input().split())
y = (g/w) * 1000
res = y

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    x = (a/b)*1000
    if x < res :
        res = x

print(round(res,2))