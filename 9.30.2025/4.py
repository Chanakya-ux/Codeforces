import sys
def solve():
    n = int(input())
    s = list(map(int,input().split()))
    x = abs(s[0])
    c = False
    S =[abs(p) for p in s]
    S.sort()
    if n==1 or n==2:
        print("YES")
        return
    if  x==S[n-1]:
        c = True
    
    if   c:
        print("NO")
    else:
        print("YES")
def main():
    t = int(input())
    for _ in range(t):
        solve()
if __name__=="__main__":
    main()