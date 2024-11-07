n = int(input())

for i in range(n):
    input_coin = input().split()
    a = int(input_coin[0])
    coin = list(map(int,input_coin[1:]))

    good = True
    for j in range(1,a):
        if coin[j] < 2 * coin[j-1]:
            good = False
            break

    print("Denominations:", " ".join(map(str, coin)))
    if good:
        print("Good coin denominations!\n")

    else:
        print("Bad coin denominations!\n")