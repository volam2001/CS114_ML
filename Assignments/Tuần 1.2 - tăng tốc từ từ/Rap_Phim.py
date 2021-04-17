import math
n,m,a = [int(x) for x in input().split()]
if n % a == 0 and m % a == 0:
    print((n//a)*(m//a))
else:
    print(math.ceil(n/a)*math.ceil(m/a))
