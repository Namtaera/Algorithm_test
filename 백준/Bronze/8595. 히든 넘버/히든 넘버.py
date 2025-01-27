import re

# 입력 처리
n = int(input())  # 문자열의 길이 (사용하지 않아도 무방)
word = input().strip()  # 단어 입력

# 정규식을 사용하여 모든 연속된 숫자 추출
numbers = re.findall(r'\d{1,6}', word)  # 최대 6자리 숫자를 추출

# 추출된 숫자를 정수로 변환 후 합산
total_sum = sum(map(int, numbers))

# 결과 출력
print(total_sum)
