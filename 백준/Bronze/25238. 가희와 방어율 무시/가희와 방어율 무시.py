a, b = map(int, input().split())

b_per = a * (b * 0.01)

era = a-b_per

if era >= 100 :
    print(0)

else :
    print(1)