def quickSort(l, low, high, mode):
    low = 0 if low is None else low
    high = len(l)-1 if high is None else high

    if low < high:
        pi = partition(l, low, high, mode)
        quickSort(l, low, pi, mode)
        quickSort(l, pi+1, high, mode)


def partition(l, low, high, mode):
    global count
    if mode == 0:
        pivot = l[low]
    elif mode == 1:
        pivot = l[(high + low) // 2]
    else:
        pivot = l[high-1]
    i = low -1
    j = high + 1
    # for j in range(low, high):

    #   if l[j] <= pivot:
    #     i += 1
    #     count += 1
    #     l[i], l[j] = l[j], l[i]
    while 1:
      while 1:
        i += 1
        count += 1
        if l[i] >= pivot:
          break
      while 1:
        j -= 1
        count += 1
        if l[j] <= pivot:
          break
      if i >= j:
        return j
      l[i], l[j] = l[j], l[i]
          
          
    # l[i+1], l[high] = l[high], l[i+1]
    # return i + 1


count = 0
l = [10, 99, 85, 12, 36, 47, 97, 35, 62, 44, 33, 11, 63, 13, 18, 29]
r = []
for ele in l:
    r.append(ele)

print(r)
quickSort(r, 0, len(l) - 1, 0)
print(count, '->', r)

count = 0
r = []
for ele in l:
    r.append(ele)
quickSort(r, 0, len(l) - 1, 1)
print(count, '->', r)

count = 0
r = []
for ele in l:
    r.append(ele)
quickSort(r, 0, len(l) - 1, 2)
print(count, '->', r)
