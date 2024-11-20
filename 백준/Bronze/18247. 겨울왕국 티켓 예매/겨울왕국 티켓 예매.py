T = int(input())

for i in range(T) :
    N, M = map(int, input().split())
    a = N*M
    x = (11*M) + 4

    if a < x or M<4:
        print(-1)

    else :
        print(x)