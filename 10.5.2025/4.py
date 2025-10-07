for _ in range(int(input())):
    n = int(input())
    arr = [i for i in range(1,n+1)]
    arr2=arr*2
    for i in range(n,1,-1):
        if (i+n)%i==0:
            arr2[i+n-1]=i
    print(*arr2)
