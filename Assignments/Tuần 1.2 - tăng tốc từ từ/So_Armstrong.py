n = input()
k = len(n)
s = 0
for i in range(0,k):
    s+=int(n[i])**k
if s==int(n):
    print(True)
else:
    print(False)
