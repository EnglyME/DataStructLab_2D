class Stack:
    def __init__(self,list=None):
        if list == None:
            self.items = []
            self.num = 0
            self.space = 4
        else:
            self.items = list
            self.num = len(list)
            self.space = 4 - self.num

    def pop(self):
        return self.items.pop()    
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return len(self.items) == 0
    def isFull(self):
        return len(self.items) == 4
    def peek(self):
        return self.items[-1]

    def arrive(self,i):
        if(self.num < 4):
            self.items.append(i)
            self.num +=1
            self.space -=1
        else:
            print(i,'SOI FULL')
    def depart(self,i):
        if i in self.items:
            self.space +=1
            self.num -= 1
            self.temp = []
            n = len(self.items) - 1
            while self.items[n] != i:
                self.temp.append(self.items.pop())
                n-=1
            self.items.pop()
            while self.temp != []:
                self.items.append(self.temp.pop())
        elif self.items == []:
            print('Cant depart :Soi Empty')
        else:
            print('No',i)

car = Stack()
car.depart('car6')
car.arrive('car1')
car.arrive('car2')
car.arrive('car3')
car.arrive('car4')
car.arrive('car5')
print('num of car:',car.size())
print('num of space:',car.space)
print('soi have',car.items)
car.depart('car7')
car.depart('car2')
print('num of car:',car.size())
print('num of space:',car.space)
print('soi have',car.items)

