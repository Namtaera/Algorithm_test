for i in range(int(input())):
    n = int(input())
    num = [int(input()) for j in range(n)]
    res = 0
    while True :
        res += 1
        # num 안의 숫자들을 res 나눈 나머지가 서로 다른 것이 n개인가를 확인
        if len({j%res for j in num}) == n: 
            print(res)
            break