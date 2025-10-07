import sys
def solve():
    n,x = map(int,sys.stdin.readline().split())
    solution =[0]*n
    solution[n-1]=x
    X =x
    if n==1:
        print("0")
        return
    if n==x:
        for i in range(n):
            print(i,end=" ")
        return
    if n==1:
        print("0")
        return
    if x==0: 
        
        for i in range(n-1):
            solution[i]=i+1
        print(*solution)
        return
    else:
        for i in range(n):
            X-=1
            solution[i]=X
            if X==0:
                break
        N =n
        for j in range(i+1,n-1):
            N-=1
            solution[j]=N
        
    print(*solution)
def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        solve()
if __name__=="__main__":
    main()
