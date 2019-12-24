
class Node:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left if left else None
        self.right = right if right else None

    def __str__(self):
        return str(self.data)

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
        return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)


def printSideway(root, level):
    if root:
        printSideway(root.right, level+1)
        s=''
        if level > 1:
            s = ' '
        print('    '*level, root.data, sep=s)
        printSideway(root.left, level+1)


def minValue(root):

    t = root
    while t.left != None:
        t=t.left

    return t

def _minValue(node):
        if node.left is None:
            return node
        else:
            return _minValue(node.left)


def deleteNode(root, data):

    if root is None:
        return None


    if data < root.data:
        root.left = deleteNode(root.left, data)
    elif data > root.data:
        root.right = deleteNode(root.right, data)
    else:

        if root.right == None:
            temp = root.left
            return temp
        elif root.left == None:
            temp = root.left

        temp = _minValue(root.right)  # find inorder successor        
        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)

    return root

# sum all
def sumAll(root):
    global total
    if root:
        total += root.data
        sumAll(root.left)
        sumAll(root.right)

# sum all 2
def sumAll2(root):
    if root is None:
        return 0
    else:
        return root.data + sumAll2(root.left) + sumAll2(root.right)

# sum of leaf
def sumLeaf(root):
    global lTotal
    if root:
        if (root.left is None and root.right is None):
            lTotal += root.data
        sumLeaf(root.left)
        sumLeaf(root.right)

# sum of non leaf
def sumNonLeaf(root):
    global nTotal
    if root and (root.left != None or root.right != None):
        nTotal += root.data
        sumNonLeaf(root.left)
        sumNonLeaf(root.right)

# product of all nodes
def productAll(root):
    if root is None:
        return 1
    else:
        return root.data * productAll(root.left) * productAll(root.right)


l = [5,4,3,2,1,1,2,3,4,5]
print ('input', l)
t = None
for ele in l:
    t = insert(t, ele)
print('inorder: ', end='')
inorder(t)
print()
print('prinSideway: ')
printSideway(t, 0)
print('===============================')
#print(deleteNode(t, 4))
#print('prinSideway: ')
#printSideway(t, 0)
#print('===============================')
print("sumLeaf")
lTotal = 0
sumLeaf(t)
print(lTotal)
print("sumNonLeaf")
nTotal = 0
sumNonLeaf(t)
print(nTotal)
print("sumAll")
total = 0
sumAll(t)
print(total)
print("sumAll2")
print(sumAll2(t))
print("product of all nodes")
print(productAll(t))