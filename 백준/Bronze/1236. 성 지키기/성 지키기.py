n, m = map(int, input().split())
l = []
x, y = 0, 0

for i in range(n) :
   l.append(input())

for j in range(n) :
    if "X" not in l[j] :
        x += 1 

for k in range(m) : # 여기부터 블로그 참고
    if "X" not in [l[j][k]  for j in range(n)]:
        y += 1

print(max(x, y))