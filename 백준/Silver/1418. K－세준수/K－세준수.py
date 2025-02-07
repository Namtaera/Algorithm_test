n = int(input())
k = int(input())

a = [0] * (n+1)

for i in range(2, n+1) :
    if a[i] == 0:
        for j in range(i,n+1,i):
            if j % i == 0:
                a[j] = max(a[j], i)

num = 0
for i in a:
    if i <= k:
        num += 1

print(num-1)
# 에라토스테네스의 체 참고