import sys
x = int(input())
while x>0:
        n,k = sys.stdin.readline().split()
        a = sys.stdin.readline().split()
        print(a.count(k))
        x-=1
