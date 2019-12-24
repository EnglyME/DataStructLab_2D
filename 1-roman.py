def roman_iterative(num):
    sr = ''
    while num > 0:
        if num >= 1000:
            sr += 'm'
            num -= 1000
        elif num >= 900:
            sr += 'cm'
            num -= 900
        elif num >= 500:
            sr += 'd'
            num -= 500
        elif num >= 400:
            sr += 'cd'
            num -= 400
        elif num >= 100:
            sr += 'c'
            num -= 100
        elif num >= 90:
            sr += 'xc'
            num -= 90
        elif num >= 50:
            sr += 'l'
            num -= 50
        elif num >= 40:
            sr += 'xl'
            num -= 40
        elif num >= 10:
            sr += 'x'
            num -= 10
        elif num >= 9:
            sr += 'ix'
            num -= 9
        elif num >= 5:
            sr += 'v'
            num -= 5
        elif num >= 4:
            sr += 'iv'
            num -= 4
        elif num >= 1:
            sr += 'i'
            num -= 1
    return sr


def roman_recursive(num):
    sr = ''
    if num == 0:
        return sr
    else:
        if num >= 1000:
            sr += 'm'
            num -= 1000
        elif num >= 900:
            sr += 'cm'
            num -= 900
        elif num >= 500:
            sr += 'd'
            num -= 500
        elif num >= 400:
            sr += 'cd'
            num -= 400
        elif num >= 100:
            sr += 'c'
            num -= 100
        elif num >= 90:
            sr += 'xc'
            num -= 90
        elif num >= 50:
            sr += 'l'
            num -= 50
        elif num >= 40:
            sr += 'xl'
            num -= 40
        elif num >= 10:
            sr += 'x'
            num -= 10
        elif num >= 9:
            sr += 'ix'
            num -= 9
        elif num >= 5:
            sr += 'v'
            num -= 5
        elif num >= 4:
            sr += 'iv'
            num -= 4
        elif num >= 1:
            sr += 'i'
            num -= 1
            print(num)
    return sr + roman_recursive(num)


print("Convert Decimal to Roman number", end='')
num = int(input("Enter Decimal number : "))
print("Roman number Iterative : ", roman_iterative(num), sep='')
print("Roman number Recursive : ", roman_recursive(num), sep='')
