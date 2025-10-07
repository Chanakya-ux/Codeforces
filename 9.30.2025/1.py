import sys
def solve():
    n,k = map(int,sys.stdin.readline().split())
    s = list(sys.stdin.readline().strip())
    ones=s.count('1')
    zeroes=s.count('0')
    c = abs(ones-zeroes)//2
    if ones ==0 or zeroes ==0:
        if len(s)//2==k:
            print("YES")
        else:
           print("NO")
        return
    if (k-c)%2==0 and k>= c:
        print("YES")
    else:
        print("NO")

def main():
    t = int(sys.stdin.readline())    
    for _ in range(t):
        solve()
if __name__=="__main__":
    main()