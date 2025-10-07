def diagonal(j,s,n):
    
    minn=min(s[a][j+a] for a in range(n-j))
    if minn<0:
        return minn
    else:
        return 0
def diagonal2(i,s,n):
    
    minn=min(s[a+i][a] for a in range(n-i))
    if minn<0:
        return minn
    else:
        return 0    
    

for _ in range(int(input())):
    n = int(input())
    s=[]
    for _ in range(n):
        s.append(list(map(int,input().split())))
    count=0
    for j in range(n):
        count +=diagonal(j,s,n)
    for i in range(1,n):
        count+=diagonal2(i,s,n)
    print(-1*count)

#2033B