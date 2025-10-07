from collections import Counter
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    c = Counter(l)
    x = sum(1 for count in c.values() if count==1)
    y = sum(1 for m in c.values() if m!=1)
    print(x+y+1 if x%2 else x +y)