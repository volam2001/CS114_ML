import sys
def remove_values_from_list(the_list, val):
	return [value for value in the_list if value != val]

l = []
while True:
	k = sys.stdin.readline()
	a= list(map(int, k[:len(k)-1].split()))
	if a[0] == 0:
		l = [a[1]]+l
	elif a[0] == 1:
		l.append(a[1])
	elif a[0] == 2:
		try:
			index = l.index(a[1])
			l.insert(index+1,a[2])
			continue
		except:
			l = [a[2]]+l
	elif a[0] == 3:
		try:
			index = l.index(a[1])
			l.pop(index)
		except:
			continue
	elif a[0] == 4:
		l = remove_values_from_list(l, a[1])
	elif a[0] == 5:
		if len(l)>0:
			l.pop(0)
	elif a[0] == 6:
		break
for i in l:
	print(i,end = " ")
