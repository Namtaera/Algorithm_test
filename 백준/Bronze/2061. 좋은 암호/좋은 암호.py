k, l = map(int,input().split())
a = 0

for i in range(2, l):
    if k%i == 0:
        print("BAD", i)
        a = k/i
        break

else:
    print("GOOD")
    