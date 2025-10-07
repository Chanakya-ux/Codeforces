t = int(input())
for _ in range(t):
    n, k  = [int(x) for x in input().split()]
    L = list(range(1, n + 1))
    print(*[x//k if x%k == 0 else x + n//k - x//k for x in L])