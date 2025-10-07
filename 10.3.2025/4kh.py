for i in[*open(0)][1:]:
	b,a=map(int,i.split());d=[];c=1
	for j in range(1,b+1):
		if j%a:d.append(b);b-=1
		else:d.append(c);c+=1
	print(*d)