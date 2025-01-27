# 입력받을 테스트 케이스의 수
n = int(input())

# 각 테스트 케이스를 처리
for i in range(n):
    # 각 테스트 케이스에서 총 길이와 '#'을 제외한 길이를 저장
    tmp = [0, 0]  # tmp[0]: 전체 문자 길이, tmp[1]: '#' 제외한 문자 길이
    
    # 한 줄씩 입력을 받음
    while True:
        l = input()
        
        # 입력이 빈 줄이면 종료
        if l != "":
            # 전체 길이를 tmp[0]에 추가
            tmp[0] += len(l)
            # '#' 문자를 제외한 길이를 tmp[1]에 추가
            tmp[1] += len(l) - l.count('#')
        else:
            break
    
    # 효율성 비율 계산: (총 길이 중 '#' 제외한 비율 * 100)
    sum = round(tmp[1] / tmp[0] * 100, 1)
    
    # 소수점 여부에 따라 출력 포맷 결정
    if sum % 1 == 0:  # 정수로 나누어 떨어질 경우
        print("Efficiency ratio is %d%%." % int(sum))
    else:  # 소수점이 있을 경우
        print("Efficiency ratio is %.1f%%." % sum)
