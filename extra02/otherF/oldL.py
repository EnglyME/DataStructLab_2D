# Q1 
# Sum Even

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def sumEven(l, n):

	if n >= 0:
		if l[n] % 2 == 0:
			return l[n] + sumEven(l, n-1)
		else:
			return sumEven(l, n-1)
	else:
		return 0

print("Q1:")
print(sumEven(l, len(l)-1))


# Q2 : tree  เบิ้ลค่าที่มากกว่า ค่าinput
# double value of the node
# that the value more than the "input"
# def doubleMore(r,val) : # r for root & val for input value
print('------------------------')
class Node:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left if left else None
		self.right = right if right else None

def printSideway(root, level=0):
	if root:
		printSideway(root.right, level+1)
		print(' ' * 4 * level, root.data, sep='')
		printSideway(root.left, level+1)

def insert(root, data):
	if root:
		if data < root.data:
			root.left = insert(root.left, data)
		else:
			root.right = insert(root.right, data)
		return root
	else:
		return Node(data)

def doubleMore(root, value):
	if root:
		if root.data > value:
			root.data *= 2
		doubleMore(root.left, value)
		doubleMore(root.right, value)


print('Q2:')

l2 = [4,10,3,6,13,9]
r = Node(7)
for e in l2:
	r = insert(r, e)

printSideway(r)

#val = int(input("Enter value: "))
doubleMore(r, 8)
print("after doubling")
printSideway(r)

print("---------------------")

# Q3
# find the rank of input value in the tree  +จนตัวที่น้อยกว่า จากซ้ายไปขวา

def rank(root, value):
	if root:
		l = rank(root.left, value)
		if root.data <= value:
			return l + rank(root.right, value) + 1
		else:
			return l
	else:
		return 0

def rank2(root, value):
	if root:
		l = rank2(root.left, value)
		r = rank2(root.right, value)
		c = 0
		if root.data <= value:
			c = 1
		return l + r + c
	else:
		return 0

print('Q3:')
print('---rank---')
print(rank(r,4))
print('---rank2---')
print(rank2(r, 4))