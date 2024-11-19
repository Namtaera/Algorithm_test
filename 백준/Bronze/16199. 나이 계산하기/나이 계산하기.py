y, m, d = map(int, input().split())
yy, mm, dd = map(int, input().split())

man = 0
count = yy-y+1
year = yy-y

if m == mm:
    if d <= dd:
        man = yy-y
    else:
        man = yy-y-1

elif m < mm:
    man = yy-y

else:
    man = yy-y-1

print(man)
print(count)
print(year)