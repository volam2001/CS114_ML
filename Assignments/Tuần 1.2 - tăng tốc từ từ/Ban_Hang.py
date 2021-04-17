import math
n = int(input())
for i in range(n):
    m = int(input())
    l = []
    l = [int(x) for x in input().split()]
    print(math.ceil(sum(l)/m))
