def sum1ToN(n):

    if n == 0:
        return 0
    else:
        return n + sum1ToN(n - 1)


def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def binarySearch(low, high, data, l):

    if low > high:
        return None

    mid = (high + low) // 2
    if data == l[mid]:
        return mid
    else:
        if data > l[mid]:
            return binarySearch(mid + 1, high, data, l)
        else:
            return binarySearch(low, mid - 1, data, l)


class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next if next is not None else None

    def __str__(self):
        return str(self.data)


def printList(h):
    if h is not None:
        print(h, end=' ')
        printList(h.next)
    else:
        print()


def createLLL(h, i):
    global l
    if i >= 0:
        last = Node(l[i], h)
        p = createLLL(last, i - 1)
        return p
    else:
        return h


def createLLL1(h, l):

    if l != []:
        node = Node(l[-1], h)
        p = createLLL1(node, l[:-1])
        return p
    else:
        return h


def createLL1ToN(h, n):

    if n >= 1:
        node = Node(n, h)
        p = createLL1ToN(node, n - 1)
        return p
    else:
        return h


l = [1, 2, 3, 4, 5]

print("==createLLL===")
h = createLLL(None, len(l) - 1)
printList(h)

print("==createLLL1===")
h1 = createLLL1(None, l)
printList(h1)

print("==createLLL2===")
h2 = createLL1ToN(None, 5)
printList(h2)


def printSack(sack, maxi):
    global good
    global name
    for i in range(maxi + 1):
        #print(good[sack[i]], end = ' ')
        print(name[sack[i]], good[sack[i]], end=' ')
    print()


def pick(sack, i, mLeft, ig):
    global N
    global good

    if ig < N:  # have something left to pick
        price = good[ig]
        if mLeft < price:  # cannot afford that ig
            pick(sack, i, mLeft, ig + 1)  # try to pick next good
        else:  # can buy
            mLeft -= price  # buy
            sack[i] = ig
            if mLeft == 0:  # done
                printSack(sack, i)
            else:  # still have money left
                pick(sack, i + 1, mLeft, ig + 1)
            # clear sack for new solutions
            pick(sack, i, mLeft + price, ig + 1)


print("==knapstacks===")
good = [20, 10, 5, 5, 3, 2, 20, 10]
name = ['soap', 'potato chips', 'loly pop',
        'toffy', 'pencil', 'rubber', 'milk', 'cookie']
N = len(good)  # numbers of good
sack = N * [-1]  # empty sack
mLeft = 20  # money left
i = 0  # sack index
ig = 0  # good index
pick(sack, i, mLeft, ig)
