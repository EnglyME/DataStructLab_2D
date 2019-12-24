class node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = None if left is None else left
        self.right = None if right is None else right
    def __str__(self):
        return str(self.data)
    def getData(self):
        return self.data
    def getLeft(self): 
        return self.left
    def getRight(self):
        return self.right
    def setData(self, data): 
        self.data = data
    def setLeft(self, left): 
        self.left = left
    def setRight(self, right): 
        self.right = right
    
class BST:
    def __init__(self, root = None):
        self.root = None if root is None else root
    
    def addI(self, data):
        if self.root is None:
            self.root = node(data)
        else:
            fatherP = None
            p = self.root
            while p:
                fatherP = p
                if data < p.data:
                    p = p.left
                else:
                    p = p.right
            if data < fatherP.data:
                fatherP.left = node(data)
            else:
                fatherP.right = node(data)
    
    def add(self, data):
        self.root = BST._add(self.root, data)
    def _add(root, data):
        if root is None:
            return node(data)
        else:
            if data < root.data:
                root.left = BST._add(root.left, data)
            else:
                root.right = BST._add(root.right,data)
        return root
    
    def inOrder(self):
        BST._inOrder(self.root)
        print()
    def _inOrder(root):
        if root:
            BST._inOrder(root.left)
            print(root.data, end=' ')
            BST._inOrder(root.right)

    def preOrder(self):
        BST._preOrder(self.root)
        print()
    def _preOrder(root):
        if root:
            print(root.data, end=' ')
            BST._preOrder(root.left)
            BST._preOrder(root.right)

    def postOrder(self):
        BST._postOrder(self.root)
        print()
    def _postOrder(root):
        if root:
            BST._postOrder(root.left)
            BST._postOrder(root.right)
            print(root.data, end=' ')
    
    def printSideway(self):
        BST._printSideway(self.root, 0)
        print()
    def _printSideway(root, level):
        if root:
            BST._printSideway(root.right, level + 1)
            print('     ' * level, root.data, sep='')
            BST._printSideway(root.left, level + 1)

    def search(self,data):
        return BST._search(self.root,data)
    def _search(root, data):
        if root is not None:
            if data < root.data:
                return BST._search(root.left, data)
            elif data > root.data:
                return BST._search(root.right, data)
            elif root.data == data:
                return root
    
    def path(self, data):
        return BST._path(self.root, data)
    def _path(root, data):
        if root:
            if data < root.data:
                print(root.data,end=' > ')
                return BST._path(root.left, data)
            elif data > root.data:
                print(root.data,end=' > ')
                return BST._path(root.right, data)
            elif root.data == data:
                return root
    
    def delete (self, data):
        return BST._delete(self.root, data)
    def _delete(root, data):
        if root:
            if data < root.data:
                root.left = BST._delete(root.left, data)
            elif data > root.data:
                root.right = BST._delete(root.right, data)
            else:
                if root.left is None:
                    temp = root.right
                    root = None
                    return temp
                elif root.right is None:
                    temp = root.left
                    root = None
                    return temp

                current = root.left
                while current.right is not None:
                    current = current.right
                temp = current
                root.data = temp.data
                root.left = BST._delete(root.left, temp.data)
            return root
        

# 14 4 9 7 15 3 18 16 20 5 16
l = [14,4 ,9 ,7 ,15 ,3 ,18, 16, 20, 5 ,16]
print(l)
t = BST()
for ele in l:
    t.addI(ele)
t.inOrder()
t.preOrder()
print(t.search(9))
print(t.path(9))
t.printSideway()
t.delete(4)
print(t.path(9))
t.printSideway()
