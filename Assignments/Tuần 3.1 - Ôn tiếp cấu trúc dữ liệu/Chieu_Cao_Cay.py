import sys
from collections import deque

class newNode: 
    def __init__(self, data): 
        self.key= data 
        self.left = None
        self.right = self.parent = None
def insert(root, key):
    newnode = newNode(key) 
    x = root 
    y = None
    while (x != None):
        y = x 
        if (key < x.key):
            x = x.left 
        else:
            x = x.right 
    if (y == None):
        y = newnode 
    elif (key < y.key):
        y.left = newnode 
    else:
        y.right = newnode 
    return y
def findHeight(root):
    if root is None:
      return 0
    return max(findHeight(root.left), findHeight(root.right)) + 1

l = deque()
while True:
    k = sys.stdin.readline()
    a = list(map(int, k[:len(k)-1].split()))
    if a[0] == 0:
        l.appendleft(a[1])
    elif a[0] == 1:
        l.append(a[1])
    elif a[0] == 2:
        try:
            index = l.index(a[1])
            l.insert(index+1,a[2])
            continue
        except:
            l.appendleft(a[1])
    else:
        break
root=None
s=set()
if len(l)!=0:
    x=l.popleft()
    s.add(x)
    root=insert(root,x)
while len(l)!=0:
    x=l.popleft()
    if x not in s:
        s.add(x)
        insert(root,x)
print(findHeight(root))
