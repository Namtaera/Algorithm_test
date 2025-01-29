n = int(input())
m = input()
k = int(input())

# 문자열에 '1'이 없거나 k가 0이면 바로 "YES" 출력
if '1' not in m or k == 0:
    print("YES")
else:
    # 문자열 끝에서 연속된 '0'의 개수 세기
    cnt = 0
    for c in reversed(m):
        if c == '0':
            cnt += 1
        else:
            break
    
    # 연속된 '0'의 개수와 k를 비교
    if cnt >= k:
        print("YES")
    else:
        print("NO")
