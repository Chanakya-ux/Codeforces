for i in range(int(input())):
    
    
        n,k = map(int,input().split())
        s = input()
        
            
        a = s.count('0')
        b = s.count('1')
        c = s.count('2')
        if c==n-a-b:
                mid = "-"*c
        else:
            if c*2>=(n-a-b):mid = "?"*(n-a-b) 
            else: mid = "?"*c+"+"*(n-a-b-2*c)+"?"*c
        print("-"*a+mid+"-"*b)   