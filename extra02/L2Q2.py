# Q2 : tree
# double value of the node
# that the value more than the "input"
# def doubleMore(r,val) : # r for root & val for input value


class Node:
    def __init__(self, data, left=None, right=None):
        self.__data = data
        self.__left = None if left is None else left
        self.__right = None if right is None else right

    def __str__(self):
        return str(self.__data)

    def getData(self):
        return self.__data

    def getleft(self):
        return self.__left

    def getRight(self):
        return self.__right

    def setData(self, data):
        self.__data = data

    def setLeft(self, left):
        self.__left = left

    def setRight(self, right):
        self.__right = right


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.getData():
        lChild = insert(root.getleft(), data)
        root.setLeft(lChild)
    else:
        rChild = insert(root.getRight(), data)
        root.setRight(rChild)
    return root


def printSideWay(root, level):
    if root is not None:
        printSideWay(root.getRight(), level+1)
        print('     '*level, root.getData())
        printSideWay(root.getleft(), level+1)


def doubleMore(root, val):
    if root:
        doubleMore(root.getRight(), val)
        if root.getData() > val:
            root.setData(root.getData()*2)
        doubleMore(root.getleft(), val)


root = None
lst = [3, 4, 5, 6, 7, 89, 2]
for i in lst:
    root = insert(root, i)
printSideWay(root, 0)
doubleMore(root, 8)
printSideWay(root, 0)
