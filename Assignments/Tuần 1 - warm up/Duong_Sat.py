k, t = [int(x) for x in input().split()]
m = t//k
if m%2==0:
    print(abs(t-k*m))
else:
    print(k-t%k)
