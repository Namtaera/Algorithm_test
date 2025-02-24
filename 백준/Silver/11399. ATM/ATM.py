n = int(input())
p = list(map(int, input().split()))
res = 0

p.sort()

for i in range(n):
    res += sum(p[0:i+1])

print(res)