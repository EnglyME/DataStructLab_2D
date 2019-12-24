# implement method
# insert [ / ]
# delete [ / ]
# search [ / ]
# smallest [ / ]
# father [ / ]
# depth [ / ]
# path [ / ]
# height
# inorder
# preorder
# postorder


class Node:
    def __init__(self, data, left=None, right=None):
        self.__data = data
        self.__left = None if left is None else left
        self.__right = None if right is None else right

    def __str__(self):
        return str(self.__data)

    def set_data(self, data):
        self.__data = data

    def set_right(self, right):
        self.__right = right

    def set_left(self, left):
        self.__left = left

    def get_data(self):
        return self.__data

    def get_right(self):
        return self.__right

    def get_left(self):
        return self.__left


def printSideWay(root, level=0):
    if root:
        printSideWay(root.get_right(), level+1)
        print('     '*level, root.get_data())
        printSideWay(root.get_left(), level+1)


def add(root, data):
    if root is None:
        return Node(data)

    if data >= root.get_data():
        root.set_right(add(root.get_right(), data))
    else:
        root.set_left(add(root.get_left(), data))
    return root


def doubleMore(root, key):
    if root:
        doubleMore(root.get_right(), key)
        doubleMore(root.get_left(), key)
        if root.get_data() > key:
            root.set_data(root.get_data()*2)


def search(root, key):
    if root:
        if root.get_data() == key:
            return root
        if key >= root.get_data():
            return search(root.get_right(), key)
        else:
            return search(root.get_left(), key)


def smallest(root):
    if root:
        if root.get_left() is None:
            return root
        else:
            return smallest(root.get_left())


def father(root, key):
    if root:
        if root.get_right():
            if root.get_right().get_data() == key:
                return root
        elif root.get_left():
            if root.get_left().get_data() == key:
                return root

        if key >= root.get_data():
            return father(root.get_right(), key)
        else:
            return father(root.get_left(), key)


def path(root, key):
    if root:
        if root.get_data() != key:
            print(root.get_data(), '  ', end=' ')
            if key >= root.get_data():
                path(root.get_right(), key)
            else:
                path(root.get_left(), key)
        else:
            print(key, end=' ')


def height(root):
    if not root:
        return -1
    else:
        l = height(root.get_left())
        r = height(root.get_right())
        if l > r:
            return l + 1
        else:
            return r+1


def depth(root, key):
    if root:
        if root.get_data() == key:
            return 0
        else:
            if key >= root.get_data():
                return depth(root.get_right(), key)+1
            else:
                return depth(root.get_left(), key)+1


# Algorithm Inorder(tree)
# 1. Traverse the left subtree, i.e., call Inorder(left-subtree)
# 2. Visit the root.
# 3. Traverse the right subtree, i.e., call Inorder(right-subtree)
def inOrder(root):
    if root:
        inOrder(root.get_left())
        print(root.get_data(), end=' ')
        inOrder(root.get_right())


# Algorithm Preorder(tree)
# 1. Visit the root.
# 2. Traverse the left subtree, i.e., call Preorder(left-subtree)
# 3. Traverse the right subtree, i.e., call Preorder(right-subtree)
def preorder(root):
    if root:
        print(root.get_data(), end=' ')
        preorder(root.get_left())
        preorder(root.get_right())


# Algorithm Postorder(tree)
# 1. Traverse the left subtree, i.e., call Postorder(left-subtree)
# 2. Traverse the right subtree, i.e., call Postorder(right-subtree)
# 3. Visit the root.
def postOrder(root):
    if root:
        postOrder(root.get_left())
        postOrder(root.get_right())
        print(root.get_data(), end=' ')


def minValue(root):
    if root:
        if not root.get_left():
            return root
        else:
            minValue(root.get_left())


def delete(root, key):
    if root is None:
        return None

    if key > root.get_data():
        root.set_right(delete(root.get_right(), key))
    elif key < root.get_data():
        root.set_left(delete(root.get_left(), key))
    else:
        if not root.get_left():
            temp = root.get_right()
            root = None
            return temp
        elif not root.get_right():
            temp = root.get_left()
            root = None
            return temp
        temp = minValue(root.get_right())
        print(temp)
        root.set_data(temp.get_data())
        root.set_right(delete(root.get_right(), temp.get_data()))
    return root


root = None
lst = [3, 5, 5, 6, 1, 1, 2, 3, 5, 123, 34, 7, 8, 8]
for i in lst:
    root = add(root, i)
doubleMore(root, 4)
printSideWay(root)
print("Search : ", search(root, 3))
print("Smallest : ", smallest(root))
print("father : ", father(root, 3))
print("path of ", end=' ')
path(root, 10)
print()
print("height : ", height(root))
print("depth", depth(root, 12))
root = delete(root, 10)
printSideWay(root)
