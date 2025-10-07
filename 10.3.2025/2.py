for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print("NO" if any(a[i] <= i * 2 or a[i] <= (n - i - 1) * 2 for i in range(n))  else "Yes")