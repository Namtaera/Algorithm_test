n = input()
x = [0] * 10

for i in range(len(n)) :
    num = int(n[i])
    if num == 6 or num == 9:
        if x[6] <= x[9]:
            x[6] += 1

        else :
            x[9] += 1

    else :
        x[num] += 1

print(max(x))