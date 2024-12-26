import sys
import re

x = sys.stdin.readlines()  # 파일처리 구글링

for i in x:
    while 'BUG' in i:  
        i = re.sub('BUG', '', i)  # 파이썬에서 문자열 수정하는 법 구글링
    print(i, end="")  
