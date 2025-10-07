import sys
def is_palindrome(s):
    S = list(str(s))
    l = len(S)
    for i in range(l):
        if S[i]!=S[l-i-1]:
            return False
    return True
def is_same(s):
    S = list(str(s))
    l = len(S)
    for i in range(l):
        if S[i]!=S[0]:
            return False
    return True
def special(s):
    S = list(str(s))
    l = len(S)
    while True:
        l = len(S)
        if S[0]==S[l-1]:
            S = S[1:-1]
        else:
            break
    return S

input = sys.stdin.readline
def solve():
    n,k = map(int,input().split())
    s = input().strip()
    l = len(s)
    if is_same(s):
        print("NO")
    else:
        if is_palindrome(s) and k==0:
            print("NO")
        elif is_palindrome(s) and k!=0:
            print("YES")
        else:
            if s[0]<s[l-1] and k==0:
                print("YES")
            elif s[0]>s[l-1] and k==0:
                print("NO")
            elif s[0]==s[l-1] and k==0:
                S = special(s)
                
                L = len(S)
                if S[0]<S[L-1]:
                    print("YES")
                else:
                    print("NO")

            elif k!=0:
                print("YES")
def main():
    t = int(input())
    for _ in range(t):
        solve()
if __name__=="__main__":
    main()