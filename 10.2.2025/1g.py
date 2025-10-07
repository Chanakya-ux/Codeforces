import sys
# Set input to read from stdin quickly for large inputs
input = sys.stdin.read

def solve():
    # Read all data and split it once
    data = input().split()
    if not data: 
        return
    
    t = int(data[0])
    results = []
    data_idx = 1
    
    for _ in range(t):
        # Read n and k
        n = int(data[data_idx])
        k = int(data[data_idx + 1])
        data_idx += 2
        
        # Read array a and convert to a set for O(1) lookups
        a = [int(x) for x in data[data_idx:data_idx + n]]
        data_idx += n
        
        s_set = set(a) 
        
        # --- 1. Count missing numbers M in the required range [0, k-1] ---
        # The number of operations required to ensure all 0 to k-1 are present.
        missing_count = 0
        # O(k) iteration
        for i in range(k):
            if i not in s_set:
                missing_count += 1
        
        # --- 2. Calculate Total Operations ---
        
        # Base operations is the count of numbers we must introduce (M).
        # These M operations use up M elements currently in the array (e.g., duplicates, or numbers > k).
        operations = missing_count
        
        # If the target number k is currently present in the array, 
        # we need one additional operation to change one instance of k 
        # to ensure it is absent (i.e., to a number outside the range [0, k]).
        if k in s_set:
            operations += 1
            
        results.append(str(operations))

    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    solve()