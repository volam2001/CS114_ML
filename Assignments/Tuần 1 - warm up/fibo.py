x = int(input())
if x<1 or x>30:
    print("So",x,"khong nam trong khoang [1,30].")
elif x==1 or x==2:
    print(1)
else:
    f1 = 1
    f2 = 1
    for i in range (3,x+1):
        f = f1 + f2
        f1 = f2
        f2 = f
    print(f2)
