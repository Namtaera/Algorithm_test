t = int(input())

for i in range (t):
    tmp = input()
    c = 0
    n = int(input())
    
    for j in range(n) :
        a = int(input())
        c += a

    if c%n == 0 :
        print("YES")

    else :
        print("NO")

