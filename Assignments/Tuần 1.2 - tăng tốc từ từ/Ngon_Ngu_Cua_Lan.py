s = input()
l = s.split()
if 'lios' in l[0] or 'etr' in l[0]:
    t=0
    c = True
    for x in l:
        if 'lios' in x and t==0:
            continue
        elif 'etr' in x and t==0:
            t=1
            continue
        elif 'initis' in x and t==1:
            t=2
            continue
        elif 'initis' in x and t==2:
            continue
        else:
            print("NO")
            c = False
            break
    if c==True:
        print("YES")

elif 'liala' in l[0] or 'etra' in l[0]:
    t=0
    c = True
    for x in l:
        if 'liala' in x and t==0:
            continue
        elif 'etra' in x and t==0:
            t=1
            continue
        elif 'inites' in x and t==1:
            t=2
            continue
        elif 'inites' in x and t==2:
            continue
        else:
            print("NO")
            c = False
            break
    if c==True:
        print("YES")
else:
    print("NO")
