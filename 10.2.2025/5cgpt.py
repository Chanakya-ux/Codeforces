from collections import Counter

def solve():
    import sys
    input = sys.stdin.readline  # faster input
    t = int(input())
    
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        
        # Use set to count presence
        present = [False] * k
        for num in a:
            if num < k:
                present[num] = True
        
        missing_count = present.count(False)   # how many in 0..k-1 are missing
        need_remove = a.count(k)               # remove all occurrences of k

        print(max(missing_count, need_remove))

# Run
solve()
