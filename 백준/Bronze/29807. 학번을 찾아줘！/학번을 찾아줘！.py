T = int(input())
lists = list(map(int,input().split()))

a = 0
b = 0
c = 0

for i in range(4, 0, -1) :
    if (len(lists) == i) : 
        for i in range (5-i) :
            lists.append(0)

if (lists[0] > lists[2]) :
    a = 508 * (lists[0] - lists[2])

elif (lists[0] < lists[2]) :
    a = 108 * (lists[2] - lists[0])

if (lists[1] > lists[3]) :
    b = (lists[1] - lists[3]) * 212

elif (lists[1] < lists[3]) :
    b = (lists[3] - lists[1]) * 305

if (lists[4] > 0) :
    c = lists[4] * 707

print((a + b + c) * 4763)