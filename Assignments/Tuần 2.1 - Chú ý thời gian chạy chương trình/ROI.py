h,w=[int(x) for x in input().split()]
arr=[]
for i in range(h):
	l=[int(x) for x in input().split()]
	arr.append(l)
top, left, bottom, right = [int(x) for x in input().split()]

i = 0
while i<=bottom:
	if i<top:
		print('0 '*w)
		i+=1
	else:
		j=0
		while j<=right:
			if j<left:
				print('0 '*left,end="")
				j=left
			else:
				print(arr[i][j],end=" ")
				j+=1
		print('0 '*(w-right-1),end='\n')
		i+=1
while i<h:
	print('0 '*w)
	i+=1
