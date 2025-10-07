import math

def solve():
    """
    Solves a single test case for The Picky Cat problem.
    """
    n = int(input())
    a = list(map(int, input().split()))

    # If n=1, the element is always the median.
    if n == 1:
        print("YES")
        return

    # The value of the first element we're interested in.
    x = abs(a[0])

    # Number of elements that must be strictly smaller than the median.
    # k = ceil(n/2) - 1
    k = math.ceil(n / 2) - 1

    count_S = 0  # Count of elements with |a_i| < x
    count_L = 0  # Count of elements with |a_i| > x

    # Categorize the other n-1 elements.
    for i in range(1, n):
        if abs(a[i]) < x:
            count_S += 1
        else:
            count_L += 1
    
    # Check the two conditions derived from our analysis.
    
    # Condition 1: Can we make -x the median?
    # This requires having at least k elements that can be made smaller than -x.
    # Only elements from Group L can do this.
    can_be_neg_median = (count_L >= k)

    # Condition 2: Can we make +x the median?
    # This requires that the number of unavoidably smaller elements (count_S)
    # does not exceed the required number of smaller elements (k).
    can_be_pos_median = (count_S <= k)

    if can_be_neg_median or can_be_pos_median:
        print("YES")
    else:
        print("NO")


def main():
    """
    Main function to handle multiple test cases.
    """
    try:
        t = int(input())
        for _ in range(t):
            solve()
    except (IOError, EOFError):
        # Handles potential empty input on some platforms
        pass

if __name__ == "__main__":
    main()