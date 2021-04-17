import sys
s = sys.stdin.readline().split()
if s[1]==s[0]:
    print(1)
else:
    s[1]= '0'+s[1]
    ans =0
    l= len(s[0])
    if s[1][-l:] >= s[0]:
        ans += 1
    ans += int(s[1][:len(s[1])-l])
    print(ans)
