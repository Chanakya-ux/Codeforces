import sys
def solve():
    n = int(sys.stdin.readline())
    powerof10 = 10
    
    solutions=[]
    while True:
            divisor = powerof10+1
            if divisor>n:
                break
            if n%divisor ==0:
                x = n//divisor
                solutions.append(x)
            powerof10*=10
    if solutions:
            solutions.sort()
            print(len(solutions))
            print(*solutions)
    else:
            print("0")
def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        solve()
if __name__ == "__main__":
    main()