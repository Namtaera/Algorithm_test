import datetime

t = list(map(int, input().split()))
d = list(map(int, input().split()))

if t[0] + 1000 < d[0]:
    print("gg")

elif t[0] + 1000 == d[0] and (t[1], t[2]) <= (d[1], d[2]):
    print("gg")

else :
    t = datetime.date(*t)
    d = datetime.date(*d)
    print("D-"+str(d.toordinal() - t.toordinal()))

# toordinal()은 두 날짜 간의 일수 차이를 계산하는 메서드 개꿀!