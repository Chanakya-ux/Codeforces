import sys
def count(s):
    left_count=0
    right_count=0
    for i in range(len(s)):
        if s[i]=='(':
            left_count+=1
        if s[i]==')':
            right_count+=1
        if left_count==right_count:
            break
    return i
            
def solve():
    s = list(sys.stdin.readline().strip())
    n = count(s)+1
    if len(s)>n:
        print("YES")
    else:
        print("NO")

    
def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        solve()
if __name__ == "__main__":
    main()
    