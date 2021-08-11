
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


    def validate_brackets(str):
        string=list(str)
        brackets=['{','[','(']
        lists=[]
        for item in string:
             if item in brackets:
              lists+=[item]
             else:
                poped_val= lists.pop()
             if  poped_val== '(':
                if item != ")":
                    return False
             if poped_val == '{':
                if item != "}":
                    return False
             if poped_val == '[':
                if item != "]":
                    return False
             if lists:
                return False
             else:
                return True

    print(validate_brackets("[({})]"))



if __name__== "__main__":
    stack = Stack()


    # stack.push("3")
    stack.validate_brackets("(")
    print(stack.peek())
