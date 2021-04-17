r,c = [int(x) for x in input().split()]
l = [0]*c
arr=[]
i=0
while i<r:
    j=0
    miniarr=[x for x in input().split()]
    while j<c:
        if miniarr[j]=='-0':
            miniarr[j]='0'
        elif miniarr[j][0]=='0' and miniarr[j][-1]!=0:
            ch=0
            while miniarr[j][ch]=='0':
                ch+=1
            miniarr[j]=miniarr[j][ch:]
        l[j]=max(l[j],len(miniarr[j]))
        j+=1
    arr.append(miniarr)
    i+=1
i=0
while i<r:
    j=0
    while j<c:
        print(' '*(l[j]-len(arr[i][j]))+arr[i][j],end="")
        j+=1
        if j<c:
            print(' ',end="")
    i+=1
    print('\n',end="")
