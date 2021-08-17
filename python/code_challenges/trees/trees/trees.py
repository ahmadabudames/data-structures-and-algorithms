from typing import final


class Binary_s_tree:

    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
        self.size = 1
    def insert(self,data):
        if self.data == data:
            return False #     duplicate data
        elif self.data > data:
            if self.left is not None:
                self.size+=1
                return self.left.insert(data)
            else:
                self.left=Binary_s_tree(data)
                self.size+=1
                return True
        else:
            if self.right is not None:
                self.size+=1
                return self.right.insert(data)
            else:
                 self.right = Binary_s_tree(data)
                 self.size+=1
                 return True


    def find(self, data):
        if self.data == data:
            return True
        elif self.data > data:
            if self.left is None:
                return False
            else:
                return self.left.find(data) #
        elif self.data < data:
            if self.right is None:
                return False
            else:
                return self.right.find(data)


    def preorder(self):
        if self is not None:
            print(self.data ,end="-->")
            if self.left is not None:
                self.left.preorder()
            if self.right is not None:
                self.right.preorder()


    def inorder(self):
        elements=[]
        if self.left:
            elements+=self.left.inorder()
        elements.append(self.data)
        if self.right:
            elements+=self.right.inorder()
        return elements

    def postorder(self):
        if self is not None:
            if self.left is not None:
                self.left.postorder()
            if self.right is not None:
                self.right.postorder()
            print(self.data , end=" ")
            return
    def is_empty(self):
        return self.size == 0
    def __str__(self):
        return self.data
    def max_tree_value(self):
       my_final =self.inorder()
       return my_final[len(my_final)-1]


    def fizz_buzz(self):
        my_final = self.inorder()
        final = []
        for i in my_final:
            if i % 3 == 0 and i % 5 == 0:
                final.append("FizzBuzz")
            elif i % 3 == 0 :
                final.append("Fizz")
            elif i % 5 == 0 :
                final.append("Buzz")
            else:
                final.append(i)
        return final


if __name__ == '__main__':
    tree = Binary_s_tree(10)
    tree.insert(3)
    tree.insert(5)
    tree.insert(7)
    tree.insert(8)
    tree.insert(15)
    tree.insert(21)
    tree.insert(20)
    tree.insert(200)
    print(tree.inorder())
    print(tree.fizz_buzz())
