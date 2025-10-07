import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    arr1 = range(n,0,-1)
    arr3= range(1,n)
    print(*arr1,n,*arr3)