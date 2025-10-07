import sys

# Read all lines from stdin, skip first 2, and take every 2nd line
for line in sys.stdin.readlines()[2::2]:
    s = list(map(int, line.split()))
    n = len(s)

    # Traverse once and swap if adjacent numbers are out of order by exactly 1
    for i in range(n - 1):
        if s[i] > s[i + 1] and s[i] - s[i + 1] == 1:
            s[i], s[i + 1] = s[i + 1], s[i]  # Pythonic swap

    # Check if the list becomes [1, 2, 3, ..., n]
    if s == list(range(1, n + 1)):
        print("YES")
    else:
        print("NO")
