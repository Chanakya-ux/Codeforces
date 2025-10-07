import bisect
import sys
from collections import Counter
input = sys.stdin.readline
def refine(S,k):
    index = bisect.bisect_right(S,k)
    return S[:index]

def solve():
    n,k = map(int,input().split())
    S = list(map(int,input().split()))
    S.sort()
    s = refine(S,k)
    kcount = s.count(k)
    freq_list = Counter(s)
    del freq_list[k]
    
    distincts = len(freq_list)
    answer = k-distincts+kcount
    print(answer)
def main():
    t = int(input())
    for _ in range(t):
        solve()
if __name__=="__main__":
    main()



