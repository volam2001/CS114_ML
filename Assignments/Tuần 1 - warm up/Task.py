n=int(input())
k=int(input())
p=int(input())
q=int(input())
x = 2*p+q-3
if x-k >= 0:
    print((x-k)//2+1, (x-k)%2+1)
elif x+k<=n-1:
    print((x+k)//2+1, (x+k)%2+1)
else:
    print(-1)
