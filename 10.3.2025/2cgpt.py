t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    def check(a):
        time = 0
        for x in a:
            time = max(time + 1, x)
        return True
    
    # Simulate left to right
    left_ok = True
    time = 0
    for x in a:
        if x < time:
            left_ok = False
            break
        time = min(x, time + 1)
    
    # Simulate right to left
    right_ok = True
    time = 0
    for x in a[::-1]:
        if x < time:
            right_ok = False
            break
        time = min(x, time + 1)
    
    print("YES" if left_ok or right_ok else "NO")
