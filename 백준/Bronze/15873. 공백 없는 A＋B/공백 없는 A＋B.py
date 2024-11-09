num = int(input())

if(num % 10 == 0):
    a = num // 100
    print(10 + a)

else :
    b = num % 10
    a = num // 10
    
    if(a == 10):
        print(10 + b)

    else :
        print(a + b)