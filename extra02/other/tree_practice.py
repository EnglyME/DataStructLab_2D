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
        s = ''
        if level > 1:
            s = ' '
        print('    '*level, root.data, sep=s)
        printSideway(root.left, level+1)


def minValue(root):

    t = root
    while t.left != None:
        t = t.left

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


l = [14, 4, 9, 7, 15, 3, 18, 16, 20, 5, 16]
print('input', l)
t = None
for ele in l:
    t = insert(t, ele)
print('inorder: ', end='')
inorder(t)
print()
print('prinSideway: ')
printSideway(t, 0)
print('===============================')
print(deleteNode(t, 4))
print('prinSideway: ')
printSideway(t, 0)
print('===============================')
