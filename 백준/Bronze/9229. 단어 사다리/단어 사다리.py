a = ""  # 이전 단어 저장
x = 0  # 테스트 케이스 종료 확인
res = "Correct"

while True:
    word = input().strip()
    
    # "#" 입력 처리
    if word == "#":
        x += 1
        if x > 1:  # 두 번째 "#" 입력 시 종료
            break
        else:
            print(res)
            res = "Correct"  
            a = ""  
            continue
    

    x = 0  
    if a == "": # 첫 번째 단어는 비교 없이 저장
        a = word
        continue
        
    # 단어 비교 로직
    if len(a) == len(word): # 길이가 같은지 확인
        m = 0 # 다른 문자의 개수를 세는 변수
        for i in range(len(a)):
            if a[i] != word[i]:
                m += 1

        if m != 1:
            res = "Incorrect"

    else :
        res = "Incorrect" # 길이 다르면 Incorrect

    a = word
