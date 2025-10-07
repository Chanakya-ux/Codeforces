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
input = sys.stdin.readline
def solve():
    n,k = map(int,input().split())
    s = input().strip()
    l = len(s)
    if n==1:
        print("NO")
    elif is_palindrome(s) and n!=1 and not is_same(s):
        if k==0:
            print("NO")
        else:
            print("YES")
    elif is_palindrome(s) and n!=1 and is_same(s):
        print("NO")  
    else:
        if k==0:
            if s[0]<s[l-1]:
                print("YES")
            elif s[0]==s[l-1] and is_palindrome(s):
                print("NO")
            elif s[0]>s[l-1]:
                print("NO")
        else:
            print("YES")
def main():
    t = int(input())
    for _ in range(t):
        solve()
if __name__=="__main__":
    main()