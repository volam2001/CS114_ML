def findCrossOver(arr, l, r, x) :  
    if (arr[r] <= x) :
        return r
    if (arr[l] > x) : 
        return l  
    mid = (l + r) // 2  
    if (arr[mid] <= x and arr[mid + 1] > x) : 
        return mid  
    if(arr[mid] < x) : 
        return findCrossOver(arr, mid + 1, r, x) 
      
    return findCrossOver(arr, l, mid - 1, x) 

def printKclosest(arr, x, k, n) : 
    r = findCrossOver(arr, 0, n - 1, x) 
    l = r - 1  
    count = 0
    result = []
    while (l >= 0 and r < n and count < k) : 
        if (x - arr[l] <= arr[r] - x) : 
            result.append(arr[l])  
            l -= 1
        else : 
            result.append(arr[r])  
            r += 1
        count += 1
    while (count < k and l >= 0) : 
        result.append(arr[l]) 
        l -= 1
        count += 1
    while (count < k and r < n) :  
        result.append(arr[r])
        r += 1
        count += 1
    result.sort()
    for i in result:
        print(i, end = " ")

n = int(input())
arr = [int(x) for x in input().split()]
k,x = [int(x) for x in input().split()]
printKclosest(arr,x,k,n)
