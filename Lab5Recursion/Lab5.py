def Fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return Fac(n - 1) * n

def sum1ToN(n):
    if n == 1:
        return 1
    else:
        return n + sum1ToN(n - 1)

def printNto1(n):
    if n != 1:
        print(n,end=' ')
        return printNto1(n - 1)
    else:
        print(n)

def printToN(n):
    if n > 0:
        printToN(n-1)
        print(n, end = ' ')

def fib(n):
    if n > 1:
        return fib(n - 1) + fib(n - 2)
    else:
        return n

def binarySearch(lo, hi, x, l):
    if hi < lo:
        return - 1
    mid = (lo + hi) // 2

    if x == l[mid]:
        return mid
    elif l[mid] < x:
        return binarySearch(mid + 1, hi, x, l)
    else:
        return binarySearch(lo, mid + 1, x, l)

def move(n, A, C, B):
    if n == 1:
        print(n, 'from', A, 'to', C)
    else:
        move(n - 1, A, B, C)
        print(n, 'from', A, 'to', C)
        move(n - 1, B, C, A)

# printNto1(5)
# printToN(5)
# print(fib(3))
# l = [1, 2, 3, 4, 5]
# print(binarySearch(1,5,3,l))

def printSack(sack, maxi):
    global good
    global name
    for i in range(maxi + 1):
        print(good[sack[i]], end=' ')
    print()

def pick(sack, i, mLeft, ig):
    global N
    global N
    global good
    if ig < N:
        price = good[ig]
        if mLeft < price:
            pick(sack, i, mLeft, ig + 1)
        else:
            mLeft -= price
            sack[i] = ig
            if mLeft == 0:
                printSack(sack, i)
            else:
                pick(sack, i + 1, mLeft, ig + 1)
            pick(sack, i, mLeft + price, ig + 1)

good = [20,10,5,5,3,2,20,10]
name = ['soap', 'potato chips', 'loly pop', 'toffy', 'pencil', 'rubber', 'milk','cookie']
N = len(good)
sack = N*[-1]
mLeft = 20
i = 0
ig = 0
pick(sack, i, mLeft,ig)
    
