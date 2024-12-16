n = int(input())
a = input().split()
b, c = map(int, input().split()) # B=총감독관 감시가능 수,  C=부감독관 감시가능 수
cnt = 0

for i in range(len(a)) :
    x = int(a[i]) - b
    cnt += 1

    if x > 0 :
        cnt += x//c
        if x%c != 0 :
            cnt += 1


print(cnt)