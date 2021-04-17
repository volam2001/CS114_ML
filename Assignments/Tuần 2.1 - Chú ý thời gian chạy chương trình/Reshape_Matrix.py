n,m=[int(x) for x in input().split()]
r,c=[int(x) for x in input().split()]
if r*c!=n*m:
	for i in range(n):
		print(input())
else:
	l=[]
	for i in range(n):
		l=l+[x for x in input().split()]
		if len(l)>=c:
			print(' '.join(l[:c]))
			l=l[c:]
	if len(l)!=0:
		print(' '.join(l))
