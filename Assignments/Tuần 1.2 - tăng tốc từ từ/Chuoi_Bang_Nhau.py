n = int(input())
for i in range(n):
    s1 = input()
    s2 = input()
    set1 = set(s1)
    set2 = set(s2)
    t = False
    for i in set1:
        if i in set2:
            print("YES")
            t = True
            break
    if t == False:
        print("NO")
