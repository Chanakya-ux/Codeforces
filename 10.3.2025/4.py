for _ in range(int(input())):
    n, k = map(int, input().split())
    l = [-1] * n                 # use -1 as empty marker
    i, j = k-1, n-k
    L = list(range(1,n+1))
    if i==j:
        l[i]=L.pop(0)
    elif i>j:
        l[i]=L.pop(0)
        l[j]=L.pop(0)
    else:
        while  len(L) >= 2 and i<n and 0<=j<n:
            l[i] = L.pop(0)
            l[j] = L.pop(0)
            i += k
            j -= k

    # fill remaining empty slots
    for p in range(n):
        if l[p] == -1 and L:
            l[p] = L.pop()

    print(*l)
