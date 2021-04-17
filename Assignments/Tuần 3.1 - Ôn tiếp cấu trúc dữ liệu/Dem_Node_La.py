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

def getLeafCount(node): 
    if node is None: 
        return 0 
    if(node.left is None and node.right is None): 
        return 1 
    else: 
        return getLeafCount(node.left) + getLeafCount(node.right) 

root=None
s=set()
x = int(input())
if x!=0:
    s.add(x)
    root = insert(root,x)
    x = int(input())
    while x!=0:
        if x not in s:
            insert(root,x)
            s.add(x)
        x = int(input())
    print(getLeafCount(root))
