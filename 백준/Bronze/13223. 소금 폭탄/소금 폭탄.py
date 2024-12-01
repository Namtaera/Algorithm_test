h, m, s = map(int, input().split(":"))
hh, mm, ss = map(int,input().split(":"))

start = h * 3600 + m * 60 + s
end = hh * 3600 + mm * 60 + ss

if end < start:
    end += 24 * 3600

diff = end - start

if diff == 0:
    print("24:00:00")
else:
    hhh = diff // 3600
    diff %= 3600
    mmm = diff // 60
    sss = diff % 60

    # 출력 형식
    print(f"{hhh:02}:{mmm:02}:{sss:02}") # 두 자리수 형식 출력방법 블로그 참고