import math


def eat(n):
    if n < 1:
        print(' '*3, 'eat', n)
    else:
        print(' '*3, 'eat', n)
        eat(n/2)


def fac(n):
    if n > 1:
        return n * fac(n-1)
    else:
        return 1


def sum1ToN(n):
    if n > 1:
        return n + sum1ToN(n-1)
    else:
        return 1


def printNTo1(n):
    if n == 1:
        print("->", " "*3, n)
    else:
        print("->", " "*3, n)
        printNTo1(n-1)


def print1ToN(n):
    if n >= 1:
        print1ToN(n-1)
        print("->", " "*3, n)


def fiboR(n):
    if n <= 1:
        return n
    else:
        return fiboR(n-1)+fiboR(n-2)


def binarySearch(lst, low, high, key):
    if high < low:
        return
    mid = math.floor(int(high+low)/2)
    if key == lst[mid]:
        return key
    elif lst[mid] < key:
        return binarySearch(lst, mid+1, high, key)
    else:

        return binarySearch(lst, low, mid-1, key)


def towerHanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod", from_rod, "to rod", to_rod)
        return
    towerHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    towerHanoi(n-1, aux_rod, to_rod, from_rod)


def sumInLst(lst):
    size = len(lst)
    if size == 1:
        return lst[0]
    else:
        return sumInLst(lst[1:]) + lst[0]


def sumInLstIdxtoIdx(lst, fromIdx, toIdx):
    if fromIdx > toIdx:
        return 0
    if fromIdx == toIdx:
        return lst[fromIdx]
    else:
        return lst[fromIdx] + sumInLstIdxtoIdx(lst, fromIdx+1, toIdx)


def printLstFW(lst):
    size = len(lst)
    if size == 1:
        print(lst[0], end=" ")
    else:
        print(lst[0], end=" ")
        printLstFW(lst[1:])


def printLstBW(lst):
    size = len(lst)
    if size == 1:
        print(lst[0], end=" ")
    else:
        printLstBW(lst[1:])
        print(lst[0], end=" ")


def appFW(lst, item):
    size = len(item)
    if size == 1:
        lst.append(item[0])
    else:
        lst.append(item[0])
        appFW(lst, item[1:])


def appBW(lst, item):
    size = len(item)
    if size == 1:
        lst.append(item[0])
    else:
        appBW(lst, item[1:])
        lst.append(item[0])


eat(11)
num = 3
print("fac", num,  "is", fac(num), sep=" ")
print("sum1To", num, "is", sum1ToN(num), sep=" ")
print("n to ", num)
printNTo1(num)
print("1 to ", num)
print1ToN(num)
print("fiboR of", num, "is", fiboR(num), sep=" ")
lst = [1, 2, 3, 4, 5, 6]
print("SUm in list ", sumInLst(lst))
print("sum from 1 to 3 ", sumInLstIdxtoIdx(lst, 1, 3))
printLstFW(lst)
print()
printLstBW(lst)
print(7)
appLSt = [7, 8, 9, 10]
appFW(lst, appLSt)
printLstFW(lst)
print()
appBW(lst, appLSt)
printLstFW(lst)