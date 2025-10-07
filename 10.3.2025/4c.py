for _ in range(int(input())):
    a,b = map(int,input().split());d=[];c=1
    for j in range(1,a+1):
        if j%b:d.append(a);a-=1
        else:d.append(c);c+=1
    print(*d)