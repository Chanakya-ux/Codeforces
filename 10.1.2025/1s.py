for _ in range(int(input())):
    n,m,p,q=map(int, input().split())
    if n%p != 0:
        print("yes")
    elif m%q == 0:
        if n!=1:
            print("yes")
        elif q==m:
            print("yes")
        else:
            print("no")
    
    else:
        print("no")