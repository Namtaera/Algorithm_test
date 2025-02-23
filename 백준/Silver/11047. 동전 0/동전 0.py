n, k = map(int, input().split())
a = []
res = 0
for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)

for i in a: # 가장 큰 동전부터 탐색
    if k == 0: 
        break # 목표 금액을 다 만들었다면 종료

    res += k//i # 해당 동전으로 사용할 수 있는 최대 개수
    k %= i # 남은 금액 업데이트
print(res)
