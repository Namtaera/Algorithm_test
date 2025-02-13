import sys

def is_covered(points, limit, w):
    """ 주어진 좌표 배열이 전체 영역을 덮을 수 있는지 확인하는 함수 """
    covered = 0.0  # 현재 덮인 범위
    for p in points:
        if p - w / 2 <= covered:
            covered = p + w / 2  # 현재 범위 확장
        else:
            return False
    return covered >= limit  # 마지막까지 덮였는지 확인

while True:
    nx, ny, w = map(float, sys.stdin.readline().split())

    if not (nx or ny or w):  # 종료 조건
        break

    xi = sorted(map(float, sys.stdin.readline().split()))
    yi = sorted(map(float, sys.stdin.readline().split()))

    if is_covered(xi, 75, w) and is_covered(yi, 100, w):
        print("YES")
    else:
        print("NO")
