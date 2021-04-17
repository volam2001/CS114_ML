s = set()
while True:
	arr=[int(x) for x in input().split()]
	if arr[0]==1:
		s.add(arr[1])
	elif arr[0]==2:
		if arr[1] in s:
			print(1)
		else:
			print(0)
	else:
		break
