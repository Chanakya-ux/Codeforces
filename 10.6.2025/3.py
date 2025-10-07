for s in [*open(0)][2::2]:
    s = s.strip()
    arr = list(map(int,s.split()))
    x,y=0,0
    nonarr = [x for x in range(1,len(arr)+1) if x not in arr]
    
    for i in range(len(arr)):
        if arr[i]==0:
            arr[i]=nonarr.pop(-1)
    
    for i in range(len(arr)):
        if arr[i]!=i+1:
            x =i
            break
    
    for j in range(1,len(arr)): 

        if arr[-j]!=len(arr)-j+1:
            y = len(arr)-j
            break
    
        
    if x and y:
        print(-x+y+1)
    else:
        print(0)
