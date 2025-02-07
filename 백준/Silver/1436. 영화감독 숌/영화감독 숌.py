# 예제를 봐도, 문제를 봐도 입력과 출력이 왜 저렇게 되는건지 이해가 되지 않아
# 질문게시판에서 문제 설명해둔 것과 참고
n = int(input())
cnt = 0
num = 666

while True:
    if '666' in str(num):
        cnt += 1

    if cnt == n:
        break

    num += 1

print(num)