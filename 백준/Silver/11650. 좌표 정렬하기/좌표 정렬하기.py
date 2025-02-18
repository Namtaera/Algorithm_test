n = int(input())
x = []

for i in range(n) :
    x.append(list(map(int, input().split())))
    
    
x.sort(key = lambda b : (b[0], b[1])) 
# lambda가 한 번 알고나면 참 쓰기 편한데 작성 법이 아직 익숙치 않아
# lambda 사용법 블로그 참고

for i in range(n):
    print(x[i][0], x[i][1])