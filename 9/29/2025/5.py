import sys
import math

def solve():
    """
    Solves a single test case for the "Left and Down" problem.
    """
    a, b, k = map(int, sys.stdin.readline().split())

    # Calculate the Greatest Common Divisor of a and b.
    g = math.gcd(a, b)

    # The required "base move" is (a/g, b/g).
    # We need to check if both components of this move are within the allowed
    # limit k. We only need to check the larger of the two components.
    if max(a // g, b // g) <= k:
        # If the base move is valid, a cost of 1 is possible.
        print("1")
    else:
        # If the base move is not valid, the minimum cost is 2.
        print("2")


def main():
    """
    Main function to handle multiple test cases.
    """
    try:
        # Read the number of test cases.
        t = int(sys.stdin.readline())
        for _ in range(t):
            solve()
    except (IOError, ValueError):
        # Handles potential empty input at the end of the file.
        pass

if __name__ == "__main__":
    main()