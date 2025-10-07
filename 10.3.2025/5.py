for _ in range(int(input())):
    a,b,c,d= map(int,input().split())
    e = c-a;f=d-b
    print("YES" if 2*min(a,b)+2>=max(a,b) and  2*min(e,f)+2>=max(e,f) else "NO")