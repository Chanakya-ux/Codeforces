def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        a = s.count('-')
        b = s.count('_')
        if a<2 or b<1:
            print("0")
        elif a%2!=0:
            print(((a**2-1)*b)//4)
        else:
            print(((a**2)*b)//4)
solve()