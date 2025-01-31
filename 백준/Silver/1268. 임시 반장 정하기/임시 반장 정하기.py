a = int(input()) 
l = []
b = [0] * a # 값 저장할 행렬
for i in range(a):
    c = list(map(int,input().split()))
    l.append(c)


for i in range(a):
    for j in range(i+1, a) :
        for k in range(5): # 5학년
            if l[i][k] == l[j][k]:  # 같은 반인 경우
                b[i] += 1
                b[j] += 1
                break


print(b.index(max(b)) + 1)
# index 중 선택하는 방식 python index관련 블로그 참고
# 행렬로 구현하는게 생각은 잘 나지만 구현이 살짝 어려웠음