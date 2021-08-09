class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self, data):
        node = Node(data)
        if not self.front:

            self.front = node
            self.rear = node
        else:

            self.rear.next = node
            self.rear = node

    def dequeue(self):
        try:
           current=self.front.data
           self.front=self.front.next
           return current
        except :
           print('empty queue')

class animal:
    def __init__(name):
        name.Cat=Queue()
        name.Dog=Queue()

    def enqueue(name,Animal,kind):
        if kind =='Cat':

            return name.Cat.enqueue(Animal)
        elif kind=='Dog':

            return name.Dog.enqueue(Animal)
        else:
            return'enter your correct animal'
    def dequeue (self,pref):
        if pref == 'Dog':
            return self.Dog.dequeue()
        if pref =='Cat':
               return self.Cat.dequeue()
        else:
            return None

if __name__=="__main__":
 q=animal()
 q.enqueue('joon','Dog')
 q.enqueue('mishmish','Cat')

 print(q.dequeue('Dog'))
 print(q.dequeue('Cat'))
 print(q.dequeue("hores"))

