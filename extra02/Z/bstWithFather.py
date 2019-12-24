class Node:
    def __init__(self, data, father=None, left=None, right=None):
        self.data = data
        self.left = None if left is None else left
        self.right = None if right is None else right
        self.father = None if father is None else father

    def __str__(self):
        return str(self.data)


def print90(root, lvl=0):
    if root:
        print90(root.right, lvl+1)
        print("     "*lvl, root.data)
        print90(root.left, lvl+1)


def printSideWay(root):
    print90(root)
    print("===================================")


def add(root, data):
    if root is None:
        return Node(data)

    if data > root.data:
        rChild = add(root.right, data)
        root.right = rChild

        rChild.father = root
    elif data < root.data:
        lChild = add(root.left, data)
        root.left = lChild

        lChild.father = root

    return root


def father(root, key):
    if root:
        if root.data == key:
            print(root.father)
        father(root.right, key)
        father(root.left, key)


def father2(root, key):
    if root:
        if root.data == key:
            return root.father

        if key >= root.data:
            return father2(root.right, key)
        else:
            return father2(root.left, key)


def minValue(root):
    if root:
        if root.left is None:
            return root
        else:
            return minValue(root.left)


def delete(root, key):
    if root is None:
        return None

    if key > root.data:
        root.right = delete(root.right, key)
    elif key < root.data:
        root.left = delete(root.left, key)
    else:
        if root.right is None:
            temp = root.left
            root = None
            return temp
        elif root.left is None:
            temp = root.right
            root = None
            return temp
        temp = minValue(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)
    return root


def largest(root):
    if root.right is None:
        return root
    else:
        return largest(root.right)


def size(root):
    if root is None:
        return 0
    return (size(root.right)+1 + size(root.left))


def largeSubtreeUntil(root, ans):

    if root is None:
        return 0

    curSum = (root.data + largeSubtreeUntil(root.left, ans) +
              largeSubtreeUntil(root.right, ans))
    ans[0] = max(ans[0], curSum)
    return curSum


def largeSubtree(root):
    if root is None:
        return 0

    ans = [-9999999999999999]
    largeSubtreeUntil(root, ans)
    return ans[0]


def sortedArrToBST(arr):
    if not arr:
        return None

    mid = len(arr) // 2
    root = Node(arr[mid])
    root.left = (sortedArrToBST(arr[:mid]))
    root.right = sortedArrToBST(arr[mid+1:])
    return root


root = None
lst = [99, 324, 3, 24, 54, 5, 435, 34, 5435]
for i in lst:
    root = add(root, i)

printSideWay(root)
delete(root, 24)
printSideWay(root)
father(root, 34)
print("father of 3 is ", father2(root, 3))
print("largest : ", largest(root))
print(size(root))
print("Large subtree is ", largeSubtree(root))
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
root = sortedArrToBST(arr)
printSideWay(root)