for s in[*open(0)][1:]:
    a=int(s.strip())
    if a ==1 or a==3: print("-1")
    elif a ==2: print("66")
    elif a ==4:print("3366")
    elif a ==6:print("333366")
    else:
        if a%2==0:
            threes = '3'*(a-2)
            print(threes+"66")
        else:
           threes = '3'*(a-4)
        
           print(threes+"6366")
    
    
