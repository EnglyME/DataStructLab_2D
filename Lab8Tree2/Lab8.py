class node:
    def __init__(self, data, left=None, right=None,father=None):
        self.data = data
        self.left = None if left is None else left
        self.right = None if right is None else right
        self.father = None if father is None else father

    def __str__(self):
        return str(self.data)
    def getData(self):
        return self.data
    def getLeft(self): 
        return self.left
    def getRight(self):
        return self.right
    def getFather(self):
        return self.father    
    def setData(self, data): 
        self.data = data
    def setLeft(self, left): 
        self.left = left
    def setRight(self, right): 
        self.right = right
    def setFather(self, father):
        self.father = father


def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data, end=' ')
        inOrder(root.right)

def add(root, data):
    if root is None:
        return node(data)
    else:
        if data < root.data:
            root.left = add(root.left, data)
        else:
            root.right = add(root.right, data)
        return root

def printSideway(root, level):
    if root:
        printSideway(root.right, level + 1)
        print('  ' * 3 * level, root.data)
        printSideway(root.left, level + 1)

def search(root, data):
    if root is None:
        return None
    if data == root.data:
        return root
    else:
        if data < root.data:
            return search(root.left, data)
        else:
            return search(root.right, data)

def path(root, data):
    if root is None:
        print('None')
    else:
        if root.data != data:
            print(root.data, end=' ')
            if data < root.data:
                path(root.left, data)
            else:
                path(root.right, data)
        else:
            print(data)

def height(root):
    if root is None:
        return -1
    else:
        hl = height(root.left)
        hr = height(root.right)
        if hl > hr:
            return hl + 1
        else:
            return hr + 1

def depth(root, data):
    if root is None:
        return -1
    if data == root.data:
        return 0
    else:
        if data < root.data:
            return depth(root.left, data) + 1
        else:
            return depth(root.right, data) + 1


l = [14, 4, 9, 7, 15, 3, 18, 16, 20, 5, 16]
print('input: ', l)

r = None
for ele in l:
    r = add(r,ele)

print('inorder: ', end=' ')
inOrder(r)
print()

print('printSideway: ')
printSideway(r, 0)

print('height of ', r.data, '=', height(r))

d = 5
print('path:', d, '=', end=' ')
path(r, d)

d = 9
t = search(r, d)
print(t.data)

d = 18
print('depth of node data ', d, '=', depth(r, d))

    

        
        