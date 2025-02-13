n = int(input())
a = []

for i in range(n) :
    a.append(input())

a = list(set(a)) #중복 제거 후 리스트 변환
a.sort() # 사전순
a.sort(key = len) # 길이순 -> 블로그 참고
# 사전 순 ->  길이순 순서여야 함 

for i in a :
    print(i)