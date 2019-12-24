adj = []
lst = [0, 1, 2, 3, 4, 5, 6]
adjLst = []


class Node:
    def __init__(self, data, Next=[], weight=[]):
        self.data = data
        self.weight = [] if weight is [] else weight
        self.Next = [] if Next is [] else Next

    def __str__(self):
        return str(self.data)


for i in lst:
    adjLst.append(Node(i))

adjLst[0].Next = [adjLst[1], adjLst[3]]
adjLst[0].weight = [2, 1]

adjLst[1].Next = [adjLst[3], adjLst[4]]
adjLst[1].weight = [3, 10]

adjLst[2].Next = [adjLst[0], adjLst[5]]
adjLst[2].weight = [4, 5]

adjLst[3].Next = [adjLst[2], adjLst[4], adjLst[5], adjLst[6]]
adjLst[3].weight = [2, 2, 8, 4]

adjLst[4].Next = [adjLst[6]]
adjLst[4].weight = [6]

adjLst[6].Next = [adjLst[5]]
adjLst[6].weight = [1]


def print_adj_lst(data):
    print('----------ADJ LIST')
    for i in data:
        print(str(i), end=" ")
        for j in i.Next:
            print(' > ', j, end=' ')
        print()
    print()


def print_adj_matrix(data):
    print('---------adj matrix------------')
    print(" ", end=" ")
    global adj
    for i in range(0, len(data)):
        print(i, end=' ')
    print()
    for v in data:
        print(str(v), end=' ')
        temp = []
        for i in range(0, len(data)):
            found = False
            for j in v.Next:
                if i == j.data:
                    temp.append(v.weight[v.Next.index(j)])
                    print("T", end=' ')
                    found = True
            if not found:
                temp.append(0)
                print(' ', end=' ')
        adj.append(temp)
        print()


n = len(adjLst)
known = []
distance = [float('inf')]*n
path = [None]*n
distance[0] = 0


def greedy_sort(data, distance, path):
    global n
    global known
    while len(known) != n:
        min = float('inf')
        for i in range(n):
            if i not in known and distance[i] < min:
                min_i = i
                min = distance[i]
        known.append(min_i)
        for i in range(n):
            w = adj[min_i][i]
            if w and distance[i] > min + w:
                distance[i] = min+w
                path[i] = min_i


def printPath(start, toV, distance, path):
    print('From v', start, 'to V', sep=' ')
    print('\tShortest path = ', distance[toV])
    print('\tpath : ', end=' ')
    p = path[toV]
    while p is not None:
        print('V', p, sep=' ', end=', ')
        p = path[p]
    print()


print_adj_lst(adjLst)
print_adj_matrix(adjLst)
greedy_sort(adj, distance, path)
printPath(0, 5, distance, path)