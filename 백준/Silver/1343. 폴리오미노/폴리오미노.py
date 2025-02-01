n = input()

n = n.replace("XXXX", "AAAA")
n = n.replace("XX", "BB")

if "X" in n:
    print(-1)

else:
    print(n)

# 반복문 사용해서 하다가 갑자기 replace함수가 떠올라 쉽게 해결