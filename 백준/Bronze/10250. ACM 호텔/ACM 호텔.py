t=int(input())
for i in range(t):
    h,w,n=map(int,input().split())
    hx=n%h*100
    x=n//h+1
    if n%h==0:
        hx=h*100
        x=n//h
    print(hx+x)

