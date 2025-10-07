for _ in range(int(input())):
    n,a,b,c,d = map(int,input().split())
    x,y=0,0
    if a>c:
        x = n-c
    elif a<c:
        x =c
    if b>d:
        y = n-d
    elif b<d:
        y = d
    print(max(x,y))