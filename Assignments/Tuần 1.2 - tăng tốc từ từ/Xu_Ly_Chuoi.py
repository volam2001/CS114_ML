s = input()
n = ['a','o','y','e','u','i']
s = s.lower()
i = 0
while i<len(s):
    if s[i] in n:
        s = s[0:i]+s[i+1:]
        i-=1
    i+=1
result = ''
i=0
while i<len(s):
    result = result + '.' + s[i]
    i+=1
print(result)
