import sys

def solve():
    """
    Solves a single test case for The Secret Number problem.
    """
    n = int(sys.stdin.readline())
    
    solutions = []
    
    # We iterate through k=1, 2, 3... by building the divisor 1 + 10^k
    power_of_10 = 10  # Starts with 10^1
    
    while True:
        divisor = 1 + power_of_10
        
        # If divisor > n, then x would be < 1, which is not allowed.
        # We can stop checking.
        if divisor > n:
            break
            
        # Check if n is perfectly divisible by (1 + 10^k)
        if n % divisor == 0:
            x = n // divisor
            solutions.append(x)
            
        # Prepare for the next k by multiplying by 10
        power_of_10 *= 10

    if not solutions:
        print(0)
    else:
        # Sort the results and print in the required format
        solutions.sort()
        print(len(solutions), *solutions)

def main():
    """
    Main function to handle multiple test cases.
    """
    try:
        num_test_cases = int(sys.stdin.readline())
    except (IOError, ValueError):
        num_test_cases = 0

    for _ in range(num_test_cases):
        solve()

if __name__ == "__main__":
    main()