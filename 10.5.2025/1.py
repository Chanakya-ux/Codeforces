for s in [*open(0)][2::2]:
    s=list(map(int,s.split()))
    for i in range(len(s)-1):
        if s[i]>s[i+1] and abs(s[i]-s[i+1])==1:
            j = s[i+1]
            s[i+1]=s[i]
            s[i]=j
    
    p = [p for p in range(1,len(s)+1)]
    #p = ''.join(map(str,p))
    if s ==p:
        print("yes")
    else:
        print("NO")

