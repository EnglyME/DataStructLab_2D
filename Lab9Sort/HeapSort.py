class LinkedList:

  class Node:
    def __init__( self, data, next=None ):
      self.data = data
      self.next = next
    
    def __str__( self ):
      return str(self.data)

  def __init__( self ):
    self.head = self.Node(None)
  
  def __str__( self ):
    linked_data = ''
    p = self.head.next
    while p is not None:
      linked_data += str(p.data)
      linked_data += ' -> ' if p.next is not None else ''
      p = p.next
    return linked_data
  
  def __len__( self ):
    p = self.head.next
    count = 0
    while p is not None:
      count += 1
      p = p.next
    return count
  
  def index( self, i ):
    p = self.head.next
    for _ in range(i):
      if p.next is not None:
        p = p.next
      else:
        return None
    return p
  
  def append( self, data ):
    p = self.head
    while p.next is not None:
      p = p.next
    new_node = self.Node(data)
    p.next = new_node


def print90(l, i=0, level=0):
    if i in range(len(l)):
        print90(l, (i * 2) + 2, level+1)  # R
        print('   ' * level, l.index(i), sep='')
        print90(l, (i * 2) + 1, level + 1)  # L


def insertMin(l, data):
    l.append(data)
    hpfyMin(l)
    
def hpfyMin(l, cur=None):
    cur = len(l) - 1 if cur is None else cur
    before = int(cur // 2 if cur % 2 == 1 else(cur / 2) - 1)
    if before in range(len(l)):
        if l.index(cur).data < l.index(before).data:
            l.index(cur).data, l.index(before).data = l.index(before).data, l.index(cur).data
        hpfyMin(l,before)            


def deleteMin(l, last=None, d=None, i=0):
    deleted = l.index(i).data if d is None else d
    last = len(l) - 1 if last is None else last
    left = l.index(i * 2 + 1).data if i * 2 + 1 <= last else None
    right = l.index(i * 2 + 2).data if i * 2 + 2 <= last else None

    if right is None:
        if left is None:
            l.index(last).data = deleted
            return deleted
        else:
            l.index(i).data = left
            return deleteMin(l, last, deleted, i * 2 + 1)
    else:
        if left < right:
            l.index(i).data = left
            return deleteMin(l, last, deleted, i * 2 + 1)
        else:
            l.index(i).data = right
            return deleteMin(l, last, deleted, i * 2 + 2)


h = LinkedList()
l = [68, 65, 32, 24, 26, 21, 19, 13, 16, 14]
for ele in l:
    print('insert:', ele)
    insertMin(h, ele)
    print(h)
    print90(h)
    print('_______________')


s = []
print('\n ----DELETE----')
for i in reversed(range(1, len(h))):
    last = h.index(i)
    tmp = deleteMin(h, i)
    print('deleteMin:', tmp, 'FindPlaceFor:', last)
    print(h)
    print90(h)
    print('_______________')
    s.append(tmp)

print('Sort:', s)
