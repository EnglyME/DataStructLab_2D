class node:
	def __init__(self,data,next=None):
		self.data = data
		if next is None:
			self.next = None
		else:
			self.next = next
	def __str__(self):
		return str(self.data)
	def getData(self):
		return self.data
class list:
	def __init__(self,head=None):
		self.head = head
		if head == None:
			self.size = 0
		else:
			self.size = 1
	def __str__(self):
		s = ''
		temp = self.head
		if self.size == 0:
			return 'no member in list'
		while temp.next != None:
			s = s + temp.data
			temp = temp.next
		return s + temp.data

	def size(self):
		if self.head == None:
			return 0
		else:
			temp = self.head
			num = 0
			while temp:
				num += 1
				temp = temp.next
			return num
	def getSize(self):
		return self.size
	def isEmpty(self):
		return self.size == 0
	def append(self,data):
		p = node(data)
		if self.head == None:
			self.head = p
		else:
			t = self.head
			while t.next != None:
				t = t.next
			t.next = p
		self.size += 1
	def addHead(self, data):
		q = node(data,self.head)
		self.head = q
		self.size += 1
	def isIn(self,data):
		temp = self.head
		while temp.data != data and temp.next != None:
			temp = temp.next
		return temp.data == data
	def before(self,data):
		temp = self.head
		n = 0
		if self.size == 0:
			print('cant find because no member in list')
		else:
			while temp.data != data and temp.next != None:
				temp = temp.next
				n+=1
			temp = self.head
			for i in range(n - 1):
				temp = temp.next
			return temp.data
	def removeHead(self):
		if self.size == 0:
			print('cant remove because no member in list')
		else:
			self.head = self.head.next
			self.size -= 1
	def removeTail(self):
		temp = self.head
		while temp.next != None:
			pre = temp
			temp = temp.next
		pre.next = None
		self.size -= 1
	def remove(self,data):
		if self.isIn(data):
			temp = self.head
			if(temp.data == data):
				self.head = self.head.next
			else:
				while temp:
					if temp.data == data:
						rem = temp
						break
					bef = temp
					temp = temp.next
				bef.next = temp.next
			self.size -= 1

		else:
			return str(data) + ' not found in the list'

#l = list()
#l.append('a')
#l.append('b')
#l.append('c')
#l.append('d')
#print(l.size)
#print(l.getSize())
#print(l.before('b'))
#l.remove('b')
#print(l.__str__())
#l.removeHead()
#print(l.__str__())

