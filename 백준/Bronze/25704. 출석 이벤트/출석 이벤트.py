n = int(input())
p = int(input())
sale = 0
if n >= 5 and n < 10 :
    p = p-500

elif n >= 10 and n < 15 :
    sale = p * 0.1
    if sale < 500 :
        sale = 500
    p = p-sale

elif n >= 15 and n < 20 :
    sale = p * 0.1
    if sale < 2000 :
        p = p - 2000
        
    else : 
        p = p - sale
        

elif n >= 20 :
    sale = p * 0.25
    if sale < 2000 :
        p = p-2000

    else :
        p = p-sale

if (p<0) :
    p = 0
    
print(int(p))