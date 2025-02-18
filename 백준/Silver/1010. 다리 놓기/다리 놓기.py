import math

t = int(input()) 

for i in range(t):
    n, m = map(int, input().split())

    res = math.comb(m,n) # math.comb를 모르고 버텨왔던 시간이 무력하다.

    print(res)
