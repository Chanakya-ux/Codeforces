
import sys
input = sys.stdin.readline

def solve():
    S =[]
    
    n = int(input())
    for _ in range(n):
        S += list(map(int,input().split()))
    
    
    l = len(S)
    S_left = S[:len(S)//n]
    

    
    S_right = S[(((n-1)*l)//n)+1:]
    
    S_new = S_left + S_right 
    
    x =0 
    s_new_set = set(S_new)  
    for i in range(1,2*n+1):
        if i not in s_new_set:
            x = i
            break
    
    S_new.insert(0,x)
    if n==1 and S[0]==1:
        X= [2,1]
        print(*X)
    elif n==1 and S[0]==2:
        X = [1,2]
        print(*X)
    else:
        print(*S_new)

def main():
    t = int(input())
    for _ in range(t):
        solve()
if __name__ == "__main__":
    main()
    
