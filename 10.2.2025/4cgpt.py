t = int(input())
def is_same(s):
    S = list(str(s))
    l = len(S)
    for i in range(l):
        if S[i]!=S[0]:
            return False
    return True
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    rev = s[::-1]

    if s < rev:
        print("YES")
    elif is_same(s):
        print("NO")
        
    elif s == rev and k==0:
        print("NO")
    elif s== rev and k!=0:
        print("YES")
    elif k == 0:
        print("NO")
    elif n == 1:
        print("NO")
    else:
        # If k > 0 and n > 1, we can always rearrange to make s universal
        print("YES")
