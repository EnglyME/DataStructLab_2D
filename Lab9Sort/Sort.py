class LinkedList:

    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

        def __str__(self):
            return str(self.data)

    def __init__(self):
        self.head = self.Node(None)

    def __str__(self):
        linked_data = ''
        p = self.head.next
        while p is not None:
            linked_data += str(p.data)
            linked_data += ' -> ' if p.next is not None else ''
            p = p.next
        return linked_data

    def __len__(self):
        p = self.head.next
        count = 0
        while p is not None:
            count += 1
            p = p.next
        return count

    def index(self, i):
        p = self.head.next
        for _ in range(i):
            if p.next is not None:
                p = p.next
            else:
                return None
        return p

    def append(self, data):
        p = self.head
        while p.next is not None:
            p = p.next
        new_node = self.Node(data)
        p.next = new_node


def bubbleSort(l):
    n = len(l)
    for i in reversed(range(n)):
        for j in range(i):
            if l.index(j).data > l.index(j + 1).data:
                l.index(j).data, l.index(
                    j + 1).data = l.index(j + 1).data, l.index(j).data


def selectionSort(l):
    n = len(l)
    for last in reversed(range(n)):
        big = last
        for i in range(last):
            if l.index(i).data > l.index(big).data:
                big = i
        l.index(big).data, l.index(last).data = l.index(
            last).data, l.index(big).data


def insertionSort(l):
    n = len(l)
    for i in range(1, n):
        insertEle = l.index(i).data
        for ip in reversed(range(i + 1)):
            if insertEle < l.index(ip-1).data and ip > 0:
                l.index(ip).data = l.index(ip-1).data
            else:
                l.index(ip).data = insertEle
                break


def mergeSort(l, left, right):
    mid = (left + right) // 2
    if left < right:
        mergeSort(l, left, mid)
        mergeSort(l, mid + 1, right)
        merge(l, left, mid + 1, right)


def merge(l, left, right, rightEnd):
    start = left
    leftEnd = right - 1
    result = []
    #print('left=', l[start:leftEnd + 1], '\t right=', l[right:rightEnd + 1])
    while left <= leftEnd and right <= rightEnd:
        if l.index(left).data < l.index(right).data:
            result.append(l.index(left).data)
            left += 1
        else:
            result.append(l.index(right).data)
            right += 1
    while left <= leftEnd:
        result.append(l.index(left).data)
        left += 1
    while right <= rightEnd:
        result.append(l.index(right).data)
        right += 1
    for ele in result:
        l.index(start).data = ele
        start += 1
        if start > rightEnd:
            break


def quickSort(l, low=None, high=None):
    low = 0 if low is None else low
    high = len(l)-1 if high is None else high

    if low < high:
        pi = partition(l, low, high)

        quickSort(l, low, pi-1)
        quickSort(l, pi+1, high)


def partition(l, low, high):
    i = low-1
    pivot = l.index(high).data

    for j in range(low, high):
        if l.index(j).data <= pivot:
            i += 1
            l.index(i).data, l.index(j).data = l.index(j).data, l.index(i).data

    l.index(i + 1).data, l.index(high).data = l.index(high).data, l.index(i + 1).data
    return i+1


LL = LinkedList()
l = [4, 3, 2, 1, 5, 7, 2]
# print(l)
# print(len(l))
for ele in l:
    LL.append(ele)

bubbleSort(LL)
print(LL)
selectionSort(LL)
print(LL)
insertionSort(LL)
print(LL)
mergeSort(LL, 0, len(LL) - 1)
print(LL)
quickSort(LL)
print(LL)
