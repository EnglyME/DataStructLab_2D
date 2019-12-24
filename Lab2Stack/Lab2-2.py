class Stack:
    def __init__(self,list=None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def push(self,i):
        self.items.append(i)
    def pop(self):
        return self.items.pop()    
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return len(self.items) == 0
    def peek(self):
        return self.items[-1]
s = Stack()
open_p = (['(','[','{'])
close_p = ([')',']','}'])
c = input('Enter Input: ')
for i in c:
    if i in open_p:
        s.push(i)
    elif i in close_p:
        a = close_p.index(i)
        if s.size() > 0 and open_p[a] == s.peek():
            s.pop()
print(s.items)
if (s.size() == 0):
    print('Match')
elif (s.size() != 0):
    print('Mismatch')
