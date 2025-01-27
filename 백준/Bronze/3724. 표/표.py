# 테스트 케이스 수만큼 반복 
# 이거 작성 법 파이썬 글 보고 참고함
for _ in range(int(input())):
    # m: 열의 개수 (음료의 수), n: 행의 개수 (사람의 수)
    m, n = map(int, input().split())
    
    # chart: 각 사람의 음료에 대한 평점표
    chart = []
    for i in range(n):
        # 각 사람의 평점을 차트에 추가
        chart.append([*map(int, input().split())])
    
    # 결과를 저장할 딕셔너리
    result = {}
    for i in range(m):  # 음료별로 반복
        t = 1  # 음료의 평점 곱 초기화
        for j in range(n):  # 각 사람의 평점 곱셈
            t *= chart[j][i]
        # 음료의 곱 결과를 키로, 음료 번호를 값으로 저장
        result[t] = i + 1
    
    # 가장 높은 곱을 가진 음료의 번호를 출력
    print(result[max(result)])
