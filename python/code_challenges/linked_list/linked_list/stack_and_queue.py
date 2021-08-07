from _pytest.python_api import raises


class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

class StackEmptyException(Exception):
    pass


class Stack:
    def __init__(self,node=None):
        self.top=node

    def push(self,value):
        node=Node(value)
        self.next=self.top
        self.top=node

    def pop(self):
        try:
           current=self.top.value
           self.top=self.top.next
           return current
        except:
            return 'Stack is empty'


    def peek(self):
        try:
            return self.top.value
        except:
            return 'Stack is empty'

    def is_empty(self):
        return not self.top







class Queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self, value):
        node=Node(value)
        if not self.front:
            self.front=node
            self.rear=node
        else:
            self.rear.next=node
            self.rear=node

    def dequeue(self):
        try:
           current=self.front.value
           self.top=self.front.next
           return current
        except:
            return 'Stack is empty'

    def peek(self):
         try:
            return self.front.value
         except:
            return 'The Stack is empty'

    def is_empty(self):
        return not self.front


if __name__== "__main__":
    stack = Stack()


    stack.push(3)
    print(stack.peek())























