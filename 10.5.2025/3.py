def find_0s(s):
    list0=[]
    for i,S in enumerate(s) :
        if S==0:
            list0.append(i)
    return list0
def find_1s(s):
    list1=[]
    for i,S in enumerate(s) :
        if S==1:
            list1.append(i)
    return list1
def df(list0):
    costlist0=[]
    list = list0[1:-2]
    for i in range(1,len(list0)-1):
        costlist0.append(min((list0[i]-list0[i-1]),(list0[i+1]-list0[i])))
        mapping = {list[i]:costlist0[i] for i in range(len(list))}
    return mapping

for _ in range(int(input())):
    n,q = map(int,input().split())
    c = list(map(int,input().split()))
    for _ in range(q):
        l , r = map(int,input().split())
        C = c[l-1:r+1]

