t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    l = sorted(map(int, input().split()))
    s = sorted(map(int, input().split()))

    a = sum(l)
    i = 0
    for S in s:
        i += S
        if n-i>=0:
            a -= l[n - i]  
    print(a)
