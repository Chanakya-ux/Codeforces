import sys

for _ in range(int(input())):
    n, a, b = map(int, input().split())
    s = input().strip()

    # Start coordinates
    x, y = 0, 0

    # Repeat the pattern enough times to cover required distance
    s = s * ((a+b)*2)

    found = False  # flag to mark if target reached

    for ch in s:
        if ch == "N":
            y += 1
        elif ch == "S":
            y -= 1
        elif ch == "E":
            x += 1
        else:  # "W"
            x -= 1

        if (x, y) == (a, b):
            print("YES")
            found = True
            break

    if not found:
        print("NO")
