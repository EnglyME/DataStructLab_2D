class Queue:
	def __init__(self,list=None):
		if list == None:
			self.items = []
		else:
			self.items = list
	def enQueue(self,i):
		self.items.append(i)
	def deQueue(self):
		return self.items.pop(0)
	def isEmpty(self):
		return len(self.items) == 0
	def size(self):
		return len(self.items)
	############# ENCODE LOCK ###############
def encodeLock():
	encL = Queue()
	message = input('Enter Message: ')
	num = Queue([2,5,6,1,8,3])
	for i in range(len(message)):

		if(message[i] != chr(32)):
			n = num.deQueue()
			z = ord(message[i]) + n
			if z > 90 and z < 97:
				z = 65 + (z - 90)
			elif z > 122:
				z = 96 + (z - 122)
			encL.enQueue(chr(z))
			num.enQueue(n)
		else:
			encL.enQueue(chr(32))
	print(''.join(encL.items),end='')
	print()
	################# ENCODE INPUT #######################
def encode():
	enc = Queue()
	message = input('Enter Message: ')
	num = input('Enter num: ')
	#num = Queue([2,5,6,1,8,3])
	for i in range(len(message)):
		if(message[i] != chr(32)):
			#n = num.deQueue()
			#z = ord(message[i]) + n
			z = ord(message[i]) + ord(num[i]) - 48
			if z > 90 and z < 97:
				z = 65 + (z - 90)
			elif z > 122:
				z = 96 + (z - 122)
			enc.enQueue(chr(z))
			#num.enQueue(n)
		else:
			enc.enQueue(chr(32))
	print(''.join(enc.items),end='')
	print()
	############### DECODE LOCK #############
def decodeLock():
	encL = Queue()
	message = input('Enter Message: ')
	num = Queue([2,5,6,1,8,3])
	for i in range(len(message)):

		if(message[i] != chr(32)):
			n = num.deQueue()
			z = ord(message[i]) - n
			if z < 65:
				z = 90 - (65 - z)
			elif z > 90 and z < 97:
				z = 123 - (97 - z)
			encL.enQueue(chr(z))
			num.enQueue(n)
		else:
			encL.enQueue(chr(32))
	print(''.join(encL.items),end='')
	print()
############### DECODE INPUT ###############
def decode():
	enc = Queue()
	message = input('Enter Message: ')
	num = input('Enter num: ')
	for i in range(len(message)):
		if(message[i] != chr(32)):
			z = ord(message[i]) - ord(num[i]) + 48
			if z < 65:
				z = 91 - (65 - z)
			elif z > 90 and z < 97:
				z = 123 - (97 - z)
			enc.enQueue(chr(z))
		else:
			enc.enQueue(chr(32))
	print(''.join(enc.items),end='')
	print()
#encodeLock()
encode()
#decodeLock()
#decode()
