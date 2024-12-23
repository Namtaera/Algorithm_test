n = int(input())

if n%2 != 0 :
    a = n//2
    print("*" * n)
    print(" " * (a) + "*")

    for i in range(a) :
        print(" " * (a-i-1) + "*" + " " * (2*i+1) + "*")

else :
    print("I LOVE CBNU")