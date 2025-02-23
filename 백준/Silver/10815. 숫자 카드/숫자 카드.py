n = int(input())
n_list = list(map(int,input().split()))
m = int(input())
m_list = list(map(int,input().split()))

dic = {}

for i in m_list :
    dic[i] = 0 # 딕셔너리가 빠르대서 밸류값 출력하는 방식 사용

for i in n_list :
    if i in dic:
        dic[i] = 1 # n에 있는 값이 m에 있다면 그건 출력 1

for i in dic:
    print(dic[i], end=" ")