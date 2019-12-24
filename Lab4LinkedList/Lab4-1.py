from Lab4 import node,list

l = list()
l.append('a')
l.append('b')
l.append('c')
l.append('d')
#print(l.size)
print(l.getSize())
print(l.before('b'))
l.remove('b')
print(l)
l.removeHead()
print(l)


