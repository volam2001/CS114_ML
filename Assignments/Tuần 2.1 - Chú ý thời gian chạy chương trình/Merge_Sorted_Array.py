a,b=[int(x) for x in input().split()]
arr1=[int(x) for x in input().split()]
arr2=[int(x) for x in input().split()]
arr3=[None] * (a + b)
i = 0
j = 0
k = 0
 
while i < a and j < b:
    if arr1[i] < arr2[j]:
        arr3[k] = arr1[i]
        k = k + 1
        i = i + 1
    else:
        arr3[k] = arr2[j]
        k = k + 1
        j = j + 1
     
while i < a:
    arr3[k] = arr1[i];
    k = k + 1
    i = i + 1

while j < b:
    arr3[k] = arr2[j];
    k = k + 1
    j = j + 1

for i in arr3:
	print(i,end=" ")
