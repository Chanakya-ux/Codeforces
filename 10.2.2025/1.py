import sys
import bisect
from collections import Counter
def solve():
    n,k= map(int,input().split())
    s = list(map(int,input().split()))
    s.sort()
    if k not in s and k<n:
        i =0
        while True:
            x = k-i
            if x in s:
                break
            i+=1
        S = bisect.bisect_right(s,x)
        s_new =s[:S]
        freq_arr = Counter(s_new)
        dstinct_repeatig_nos =  sum(1 for count in freq_arr.values() if count>0 )
        tatal_reps = len(s_new)-len(freq_arr)
        answer = len(s_new)-dstinct_repeatig_nos
    else:
        S = bisect.bisect_right(s,k)
        S2 = bisect.bisect_left(s,k)
        s_new = s[:S2]
        freq_arr = Counter(s_new)
        dstinct_repeatig_nos =  sum(1 for count in freq_arr.values() if count>1 )
        tatal_reps = len(s_new)-len(freq_arr)
        answer = S-S2+tatal_reps-dstinct_repeatig_nos
        


    print(answer)
    
def main():
    t = int(input())
    for _ in range(t):
        solve()
if __name__ == "__main__":
    main()