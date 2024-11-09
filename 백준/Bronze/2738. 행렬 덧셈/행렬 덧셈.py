n, m = map(int,input().split())
dic_a = {}
dic_b = {}
dic_result = {}


for a in range(1,n+1) :
    a_nums = list(map(int,input().split()))
    dic_a[a]= a_nums
    a += 1

for b in range(1,n+1) :
    b_nums = list(map(int,input().split()))
    dic_b[b]= b_nums
    b += 1

num1 = 0
num2 = 0

for c in range(n):
    list_a = dic_a[c+1]
    list_b = dic_b[c+1]
    for d in range(m) :
        print(list_a[d] + list_b[d], end = ' ')

    print()