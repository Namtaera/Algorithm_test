import sys

# 입력 데이터 읽기
input_data = sys.stdin.read().strip().split("\n")

# 각 줄 처리
for line in input_data:
    # 입력 좌표를 나누어 숫자로 변환
    coords = list(map(float, line.split()))
    a, b, c, d, e, f, g, h = coords

    # 네 번째 점의 좌표를 초기화
    x = a + e - c
    y = b + f - d

    # 평행사변형의 성질에 따라 네 번째 점을 계산
    if a == e and b == f:
        x = c + g - a
        y = d + h - b
    elif a == g and b == h:
        x = c + e - a
        y = d + f - b
    elif c == e and d == f:
        x = a + g - c
        y = b + h - d

    # 결과 출력 (소수점 셋째 자리까지)
    print(f"{x:.3f} {y:.3f}")
