# 도대체 무슨 문제인지 이해가 안감
# 그래서 블로그 봄
import re
n = input()

start = -1
end = -1

while n.find("What", end + 1) != -1 :
    start = n.find("What", end + 1)
    end = n.find("?", start + 1)
    res = n[start:end]
    if res.find(".") != -1:
        end = n.find(".", start + 1)
        continue

    print("Forty-two" + res[4:] + ".")
