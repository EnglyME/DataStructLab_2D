from Lab4 import node,list

def bottomUp(List,percent):
	if percent > 0 and percent < 100:
		num = percent * List.getSize() / 100
		temp = List.head
		temp1 = List.head
		while temp.next != None:
			temp = temp.next
		while num - 1 != 0:
			temp1 = temp1.next
			num -= 1
		temp.next = List.head
		List.head = temp1.next
		temp1.next = None
	else:
		print('Percent should be between 0 and 100')
def riffleShuffle(List,percent):
	num = percent * List.getSize() / 100
	num2 = List.getSize() - num
	temp = List.head
	temp2 = List.head
	if List.head:
		if num >= num2:
			for i in range(0,int(num)):
				temp2 = temp2.next
			for i in range(0,int(num) - 1):
				temp = temp.next
			temp.next = None
			temp = List.head
			for i in range(0,int(num2)):
				nxt = temp.next
				nxt2 = temp2.next
				temp.next = temp2
				temp2.next = nxt
				temp = nxt
				temp2 = nxt2
		else:
			for i in range(0,int(num) - 1):
				temp2 = temp2.next
			List.head = temp2.next
			temp2.next = None
			temp2 = List.head
			for i in range(0,int(num)):
				nxt = temp.next
				nxt2 = temp2.next
				temp2.next = temp
				temp.next = nxt2
				temp = nxt
				temp2 = nxt2
	else:
		print('no member in list')

def deBottomUp(List,percent):
	if percent >= 0 and percent <= 100:
		bottomUp(List,100 - percent)
	else:
		print('Percent should be between 0 and 100')
def deRiffle(List, percent):
	temp = List.head
	temp2 = List.head
	num = percent / 100.0 * List.getSize()
	num2 = List.getSize() - num
	if percent > 0 and percent < 100:
		if num >= num2:
			temp2 = temp2.next
			nxt = temp2
			for i in range(0, int(num2) - 1):
				temp.next = temp.next.next
				temp2.next = temp2.next.next
				temp = temp.next
				temp2 = temp2.next
			temp.next = temp.next.next
			while temp.next:
				temp = temp.next
			temp.next = nxt
			temp2.next = None
		else:
			temp = temp.next
			List.head = temp
			nxt = temp2
			i = 0
			while i < num - 1:
				temp2.next = temp2.next.next
				temp.next = temp.next.next
				temp2 = temp2.next
				temp = temp.next
				i += 1
			temp2.next = temp2.next.next
			while temp2.next:
				temp2 = temp2.next
			temp.next = nxt
			temp2.next = None
	else:
		print('Percent should be between 0 and 100')

l1 = list()
for i in range(1,11):
	l1.append(str(i))
bottomUp(l1,30)
print(l1)
riffleShuffle(l1,30)
print(l1)
deRiffle(l1,30)
print(l1)
deBottomUp(l1,30)
print(l1)
