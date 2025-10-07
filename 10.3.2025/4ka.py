for t in range(int(input())):
    n,k = map(int, input().split())
 
    l = [str(i) for i in range(n//k+1, n+1)]
    for x in range(1, n//k+1):
        l.insert(k*x-1, str(x))
    print(' '.join(l))