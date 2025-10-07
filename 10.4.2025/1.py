from collections import Counter
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    c = Counter(l)
    print(1+len(c)*2-2)