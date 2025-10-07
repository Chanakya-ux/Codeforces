import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    l.sort()
    ans=0
    i=0
    j=n-1
    while i<j:
        sum = l[i]+l[j]
        if sum ==k:
            ans+=1
            i+=1
            j-=1
        elif sum>k:
            j-=1
        else:
            i+=1
    print(ans)
