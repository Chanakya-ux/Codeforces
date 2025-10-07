import sys

def solve():
    """
    Solves a single test case with the corrected logic.
    """
    try:
        n, k = map(int, sys.stdin.readline().split())
        s = sys.stdin.readline().strip()

        # Case 1: k = 0 swaps allowed.
        # The string must already be universal.
        if k == 0:
            # A string is universal if it's lexicographically smaller than its reversal.
            if s < s[::-1]:
                print("YES")
            else:
                print("NO")
            return

        # Case 2: k > 0 swaps allowed.
        # If 2k >= n, there is no middle section to work with. Impossible.
        if 2 * k >= n:
            print("NO")
            return
            
        # If 2k < n, a middle section exists.
        # Check if the outer frame of length k is a palindrome.
        prefix = s[:k]
        suffix = s[n - k:]
        
        # If the frame is palindromic, we can succeed.
        if prefix == suffix[::-1]:
            print("YES")
        else:
            print("NO")

    except (IOError, ValueError):
        # Handle potential empty lines or formatting errors in input
        return

def main():
    """
    Main function to handle multiple test cases.
    """
    try:
        num_test_cases = int(sys.stdin.readline())
        for _ in range(num_test_cases):
            solve()
    except (IOError, ValueError):
        return

if __name__ == "__main__":
    main()