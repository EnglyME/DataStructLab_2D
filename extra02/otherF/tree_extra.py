# ------------ Linked List ------------


class LNode:
    def __init__(self, data, nextNode=None):
        self.data = data
        self.next = nextNode if nextNode else None

    def __str__(self):
        return str(self.data)


def printList(head):
    print('--- print list ---')
    _printList(head)
    print()


def _printList(head):
    if head:
        print(head.data, end=' ')
        _printList(head.next)


def addL(head, data):
    return _addL(head, data)


def _addL(head, data):
    if head:
        head.next = _addL(head.next, data)
        return head
    else:
        return LNode(data)


def size(head):
    c = 0
    p = head
    while p:
        c += 1
        p = p.next
    return c

# ------------ Binary search tree ------------


class TNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left if left else None
        self.right = right if right else None

    def __str__(self):
        return str(self.data)


def insert(root, data):
    return _insert(root, data)


def _insert(root, data):
    if root:
        if data < root.data:
            root.left = _insert(root.left, data)
        else:
            root.right = _insert(root.right, data)
        return root
    else:
        return TNode(data)


def printSideway(root):
    print("--- print sideway ---")
    _printSideway(root)


def _printSideway(root, level=0):
    if root:
        _printSideway(root.right, level + 1)
        print(' ' * 4 * level, root.data, sep='')
        _printSideway(root.left, level + 1)


def search(root, value):
    print('-- search ', value, ' --', sep='')
    return _search(root, value)


def _search(root, value):
    if root:
        if value < root.data:
            return _search(root.left, value)
        elif value > root.data:
            return _search(root.right, value)
        else:
            return root


def father(root, value):
    print('--- father ---')
    if search(root, value):
        f = _father(root, value)
        print('father of', value, 'is', f)
        return f
    else:
        print('No data', value)


def _father(root, value):
    if root:
        if root.left:
            if root.left.data == value:
                return root
        if root.right:
            if root.right.data == value:
                return root

        if value < root.data:
            return _father(root.left, value)
        else:
            return _father(root.right, value)


def height(root):
    print('--- height ---')
    return _height(root)


def _height(root):
    if root:
        hl = _height(root.left)
        hr = _height(root.right)
        if hl > hr:
            return hl + 1
        else:
            return hr + 1
    else:
        return -1


def _minValue(root):
    if root.left == None:
        return root
    else:
        return _minValue(root.left)


def deleteNode(root, value):
    print('--- delete node', value, '---')
    _deleteNode(root, value)


def _deleteNode(root, value):
    if root:
        if value < root.data:
            root.left = _deleteNode(root.left, value)
        elif value > root.data:
            root.right = _deleteNode(root.right, value)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            temp = _minValue(root.right)
            root.data = temp.data
            root.right = _deleteNode(root.right, temp.data)

        return root

    else:
        return None


def depth(root, value):
    print('--- depth ---')
    if search(root, value):
        d = _depth(root, value)
        print('depth of', value, 'is', d)
    else:
        print('No data', value)


def _depth(root, value):
    if value < root.data:
        return _depth(root.left, value) + 1
    elif value > root.data:
        return _depth(root.right, value) + 1
    else:
        return 0


def linkedListToBST(head):
    print("---- linked list to tree ----")
    n = size(head)
    return _linkedListToBST(n)


def _linkedListToBST(n):
    global lin

    if n <= 0:
        return None

    left = _linkedListToBST(n // 2)
    root = TNode(lin.data)
    root.left = left

    lin = lin.next

    root.right = _linkedListToBST(n - (n // 2) - 1)
    return root


def arrayToBST(arr):
    print('---- array to tree ----')
    return _arrayToBST(arr)


def _arrayToBST(arr):
    if not arr:
        return None

    mid = len(arr) // 2
    root = TNode(arr[mid])

    root.left = _arrayToBST(arr[:mid])
    root.right = _arrayToBST(arr[mid + 1:])

    return root


def path(root, value):
    if search(root, value):
        print('path of', value, 'is', end=' ')
        _path(root, value)
        print()
    else:
        print("No data", value)


def _path(root, value):
    print(root.data, end=' ')
    if value < root.data:
        _path(root.left, value)
    elif value > root.data:
        _path(root.right, value)
    else:
        return


def countNode(root):
    print('--- count all nodes ---')
    return _countNode(root)


def _countNode(root):
    if root:
        return _countNode(root.left) + _countNode(root.right) + 1
    else:
        return 0


def countNonLeaf(root):
    print('--- count non leaf nodes ---')
    return _countNonLeaf(root)


def _countNonLeaf(root):
    if root:
        if root.left or root.right:
            return _countNonLeaf(root.left) + _countNonLeaf(root.right) + 1
        else:
            return 0
    else:
        return 0


def countLeaf(root):
    print("--- count leaf nodes ---")
    return _countLeaf(root)


def _countLeaf(root):
    if root:
        c = 0
        if root.right is None and root.left is None:
            c = 1
        return _countLeaf(root.left) + _countLeaf(root.right) + c
    else:
        return 0


def findNthNode(root, n):
    print('--- find', n, 'th node ---')
    _findNthNode(root, n)


def _findNthNode(root, n):
    global nth

    if root is None:
        return

    if nth <= n:
        _findNthNode(root.left, n)

        nth += 1
        if nth == n:
            print(root.data)

        _findNthNode(root.right, n)


def sumAll(root):
    print('--- sum of all nodes ---')
    return _sumAll(root)


def _sumAll(root):
    if root:
        l = _sumAll(root.left)
        r = _sumAll(root.right)
        return l + r + root.data
    else:
        return 0


def sumNonLeaf(root):
    print(' --- sum of non leaf nodes ---')
    return _sumNonLeaf(root)


def _sumNonLeaf(root):
    if root:
        if root.left or root.right:
            return root.data + _sumNonLeaf(root.left) + _sumNonLeaf(root.right)
        else:
            return 0
    else:
        return 0


def sumLeaf(root):
    print("--- sum leaf nodes ---")
    return _sumLeaf(root)


def _sumLeaf(root):
    if root:
        c = 0
        if (root.left is None) and (root.right is None):
            c = root.data

        return _sumLeaf(root.left) + _sumLeaf(root.right) + c
    else:
        return 0


def rank(root, value):
    print('--- rank of', value, '---')
    return _rank(root, value)


def _rank(root, value):
    if root:
        l = _rank(root.left, value)
        if root.data <= value:
            return l + _rank(root.right, value) + 1
        else:
            return l
    else:
        return 0


def rank2(root, value):
    print('--- rank2 of', value, '---')
    return _rank2(root, value)


def _rank2(root, value):
    if root:
        l = _rank2(root.left, value)
        r = _rank2(root.right, value)
        c = 0
        if root.data <= value:
            c = 1
        return l + r + c
    else:
        return 0


def productAll(root):
    print('--- product of all nodes ---')
    return _productAll(root)


def _productAll(root):
    if root:
        l = _productAll(root.left)
        r = _productAll(root.right)
        return root.data * l * r
    else:
        return 1


l = [7, 4, 10, 3, 6, 13, 9, 14, 8]
t = None
for e in l:
    t = insert(t, e)

printSideway(t)

print(search(t, 10))

father(t, 4)

print(height(t))

deleteNode(t, 7)
printSideway(t)

ll = [1, 2, 3, 4, 5, 6, 7]
lin = None
for e in ll:
    lin = addL(lin, e)
printList(lin)
tL = linkedListToBST(lin)
printSideway(tL)

arr = [1, 2, 3, 4, 5, 6, 7]
tArr = arrayToBST(arr)
printSideway(tArr)

path(tArr, 5)

print(countNode(tArr))

print(countNonLeaf(tArr))

print(countLeaf(tArr))

nth = 0
findNthNode(tArr, 9)

print(sumAll(tArr))

print(sumNonLeaf(tArr))

print(sumLeaf(tArr))

print(rank(tArr, 7))

print(rank2(tArr, 7))

print(productAll(tArr))