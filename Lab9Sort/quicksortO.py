class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class linklist:
    def __init__(self):
        self.head = node()
        self.size = 0

    def __str__(self):
        text = ''
        p = self.head.next if self.head else None
        while p:
            text += ' ' + str(p.data)
            p = p.next
        return text

    def append(self, data):
        if self.head.next is None:
            self.head.next = node(data)
            self.size += 1
            return
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = node(data)
            self.size += 1

    def getIndex(self, i) -> node:
        if i > self.size - 1:
            return
        count = 0
        p = self.head.next
        while i != count:
            count += 1
            p = p.next
        return p

    def __getitem__(self, item: int):
        return self.getIndex(item)


def quicksort(ll: linklist, low: int, high: int, mode):
    if low < high:
        p = partition(ll, low, high, mode)
        quicksort(ll, low, p, mode)
        quicksort(ll, p + 1, high, mode)


def partition(ll: linklist, low: int, high: int, mode):
    global count1
    if mode == 0:
        pivot = ll[low].data
    elif mode == 1:
        pivot = ll[(high + low) // 2].data
    else:
        pivot = ll[high - 1].data
    i = low - 1
    j = high + 1
    while 1:
        while 1:
            i += 1
            count1 += 1
            if ll[i].data >= pivot:
                break
        while 1:
            j -= 1
            count1 += 1
            if ll[j].data <= pivot:
                break
        if i >= j:
            return j
        ll[i].data, ll[j].data = ll[j].data, ll[i].data


count1 = 0
pp = linklist()
o = [10,99,85,12,36,47,97,35,62,44,33,11,63,13,18,29]

for i in o:
    pp.append(i)

print(pp)
quicksort(pp, 0, pp.size - 1, 0)
print(count1, "=>", pp)

count1 = 0
pp = linklist()
for i in o:
    pp.append(i)

quicksort(pp, 0, pp.size - 1, 1)
print(count1, "=>", pp)

count1 = 0
pp = linklist()
for i in o:
    pp.append(i)

quicksort(pp, 0, pp.size - 1, 2)
print(count1, "=>", pp)
