import sys

def solve():
    """
    Solves a single test case for the "Like the Bitset" problem.
    """
    # Read n, k, and the string s. Assume input is always valid.
    line1 = sys.stdin.readline()
    # Handle empty lines at the end of input
    if not line1:
        return
    n, k = map(int, line1.split())
    s = sys.stdin.readline().strip()

    # --- Step 1: Check for the impossible "NO" condition ---
    # A solution is impossible if there is a contiguous block of k or more '1's.
    max_consecutive_ones = 0
    current_consecutive_ones = 0
    for char in s:
        if char == '1':
            current_consecutive_ones += 1
        else:
            # Reset the counter when a '0' is found
            current_consecutive_ones = 0
        # Keep track of the longest run of '1's seen so far
        max_consecutive_ones = max(max_consecutive_ones, current_consecutive_ones)

    if max_consecutive_ones >= k:
        print("NO")
        return

    # --- Step 2: If possible, construct and print the "YES" solution ---
    print("YES")
    
    # Initialize the result permutation
    p = [0] * n
    
    # Count the '1's to know where the '0' values should start
    ones_count = s.count('1')
    
    # Initialize counters for the values to be assigned
    current_one_val = 1
    current_zero_val = ones_count + 1
    
    # Assign the permutation values in a single pass
    for i in range(n):
        if s[i] == '1':
            p[i] = current_one_val
            current_one_val += 1
        else: # s[i] == '0'
            p[i] = current_zero_val
            current_zero_val += 1
            
    # Print the final permutation with space separation
    print(*p)


def main():
    """
    Main function to handle multiple test cases.
    """
    # Read the number of test cases
    num_test_cases_str = sys.stdin.readline()
    if not num_test_cases_str:
        return
    num_test_cases = int(num_test_cases_str)

    for _ in range(num_test_cases):
        solve()

if __name__ == "__main__":
    main()