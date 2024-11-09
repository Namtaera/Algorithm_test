p1, q1, p2, q2 = map(int, input().split())

son = p1 * p2
parents = 2 * q1 * q2

if son % parents ==0 :
    print(1)

else:
    print(0)