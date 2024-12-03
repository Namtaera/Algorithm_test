T = int(input())

two = [6,2,4,8]
three = [1,3,9,7]
four = [6,4]
seven = [1,7,9,3]
eight = [6,8,4,2]
nine = [1,9]

for j in range(T) :
    a, b = map(int, input().split())
    a %= 10

    if a == 0:  
        print(10)
        
    if a == 1 or a == 5 or a == 6 :
        print(a)

    elif a == 2 :
        res = b%4
        print(two[res])
        
    elif a == 3 :
        res = b%4
        print(three[res])
        
    elif a == 7 :        
        res = b%4
        print(seven[res])
        
    elif a == 8 :
        res = b%4
        print(eight[res])

    elif a == 4:
        res = b%2    
        print(four[res])

    elif a == 9 :
        res = b%2
        print(nine[res])