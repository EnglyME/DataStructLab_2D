# Q1 : recursive function
# desin your own parameter
# return sum of "even" number in the list

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def sumEven(lst, idx=0):
    if idx < len(lst):
        if lst[idx] % 2 == 0:
            return lst[idx] + sumEven(lst, idx+1)
        else:
            return sumEven(lst, idx+1)
    else:
        return 0


print(sumEven(lst))
