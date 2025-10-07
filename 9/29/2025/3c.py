import sys
def solve():
    n,k = map(int,sys.stdin.readline().split())
    s_str =sys.stdin.readline().strip()
    s = [int(char) for char in s_str]
    mcc=0
    ccc=0
    for S in s:
        if S == 1:
            ccc+=1
        else:
            ccc=0
        mcc = max(mcc,ccc)
    count = sum(s)
    if mcc>=k:
        print("NO")
        return
    p = [0]*n
    for_0=count+1
    for_1=1
    for i in range(len(s)):
        if s[i]==1:
            p[i]=for_1
            for_1+=1
        else:
            p[i]=for_0
            for_0+=1
    print("YES")
    print(*p)
def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        solve()
if __name__ =="__main__":
    main()
