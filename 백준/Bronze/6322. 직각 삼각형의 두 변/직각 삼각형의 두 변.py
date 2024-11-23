num = 1
while True:
    a, b, c = map(int,input().split())
    if a == 0 and b == 0 and c == 0 :
        break

    if num > 1 :
        print()
    print(f"Triangle #{num}")

    if c == -1 :
        print("c = %.3f" % ((a**2+b**2)**0.5))

    elif max(a,b) >= c :
        print("Impossible.")

    elif a == -1 :
        print("a = %.3f" % ((c**2-b**2)**0.5))

    elif b == -1 :
        print("b = %.3f" % ((c**2-a**2)**0.5))

    num +=1