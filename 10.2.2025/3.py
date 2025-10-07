import sys
input = sys.stdin.readline
def no_type(n):
    if n%10 ==0:
        return True
    else :
        return False
def find_0s(n):
    power =10
    i =0
    while True:
        if n%10 !=0:
            break
        n = n//power
        
        
        i+=1
    return i,n
def cost(n):
    count=0
    N = list(str(n))
    for n in N:
        if n !='0':
            count+=1
    return count

def solve():
    c = int(input())
    if no_type(c):
        i,k = find_0s(c)
        Cost = cost(k)+i-1
    else:
        Cost = cost(c)-1
    print(Cost)
def main():
    t = int(input())
    for _ in range(t):
        solve()
if __name__=="__main__":
    main()





