def solve(s):
    x=0;y=-1
    while(x<=len(s)+y):
        for i in range(len(s)):
            if s[i]!=i+1:
                x = i
                break
        for j in range(1,len(s)+1):
            if s[-j]!=len(s)+1-j:
                y = -j
                break
        
            return len(s)-x+y+1


for s in[*open(0)][2::2]:
    l = list(map(int,s.split()))
    
    if l.count(0)>1:
        indices = [i for i,x in enumerate(l) if x==0]
        
        print(indices[-1]-indices[0]+1)
    elif l.count(0)<=1:
        index = [i for i,x in enumerate(l) if x==0]
        if index:
            value =[x for x in range(1,len(l)+1) if x not in l]
            l[index[0]]=value[0]
            
            print(solve(l))
        else:
            print(solve(l))

        



