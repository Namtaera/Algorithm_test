n = int(input())
res = 0
end = 0
l = []
for i in range(n):
    l.append(list(map(int, input().split())))

l.sort(key=lambda x: (x[1], x[0])) # 끝나는 시간 기준 정렬, 그리디

for a, b in l:
    if end <= a :
        res += 1
        end = b

print(res)