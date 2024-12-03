a, d, k = map(int, input().split())

if d == 0: 
    if a == k:  
        print(1)
    else: 
        print("X")
else:
    i = k - a  
    if i % d == 0 and (i // d) >= 0:  
        print(i // d + 1) 
    else:
        print("X") 
