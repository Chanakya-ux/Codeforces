for s in[x.strip() for x in open(0)][2::2]:
        if s.endswith("0"):
             s = s+s[-1]*2
        if s.startswith("0"):
             s = s[0]*2+s
             
        l = s.split('11')
        bad =0
        for x in l:
            if "00" not in x and x.count('0')%2:
                bad =1
        if bad:
            print("NO")
        else:
            print("yes")
