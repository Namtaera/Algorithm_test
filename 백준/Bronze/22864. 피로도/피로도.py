a, b, c, m = map(int,input().split())
# a = 일하면 피로도 쌓임
# b = 처리한 일
# c = 쉴 때 피로도 줄어들음
# m = 번아웃기준 피로도

p = 0
w = 0

for i in range(24) :
    p += a 
    if p > m :
        p -= a
        p -= c
        
    elif p <= m :
        w += b
    
    if p < 0 :
        p = 0

print(w)