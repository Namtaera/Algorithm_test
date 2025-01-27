if __name__ == '__main__':
    # 점수와 제곱 점수를 저장할 리스트
    total_scores = [0, 0, 0]
    squared_scores = [0, 0, 0]

    # 입력 처리
    n = int(input())
    
    # 이 부분 로직 블로그 참고
    for _ in range(n):
        first, second, third = map(int, input().split())
        total_scores[0] += first
        total_scores[1] += second
        total_scores[2] += third

        squared_scores[0] += first ** 2
        squared_scores[1] += second ** 2
        squared_scores[2] += third ** 2

    # 최고 점수를 찾음
    max_score = max(total_scores)

    # 최고 점수를 가진 후보자가 하나인지 확인
    if total_scores.count(max_score) == 1:
        # 단일 최고 점수를 가진 후보 출력
        winner = total_scores.index(max_score) + 1
        print(winner, max_score)
    else:
        # 점수가 동점인 경우 제곱 점수 비교
        max_squared_score = max(squared_scores)
        winner_candidates = [
            idx for idx, score in enumerate(squared_scores) if score == max_squared_score
        ]

        # 동점 후보가 여러 명이면 회장 선출 불가
        if len(winner_candidates) > 1:
            print(0, max_score)
        else:
            # 단일 후보가 있으면 회장으로 선출
            winner = winner_candidates[0] + 1
            print(winner, max_score)
