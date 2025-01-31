a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_sum = 0
b_sum = 0
res = 0

for i in range(9):
    a_sum += a[i]
    if a_sum > b_sum :
        res = 1

    b_sum += b[i]

if a_sum < b_sum and res == 1:
    print("Yes")

else :
    print("No")

# 야구 기본상식이 필요한건지 문제 설명이 빈약하다고 느껴서 오래걸림