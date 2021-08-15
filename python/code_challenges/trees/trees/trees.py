class Binary_s_tree:
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
        self.size = 0

    def insert(self,data):
        if self.data == data:
            return False #     duplicate data
        elif self.data > data:
            if self.left is not None:
                return self.left.insert(data)
                self.size+=1
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
        if self is not None:
            if self.left is not None:
                self.left.inorder()
            print(self.data ,end="-->")
            if self.right is not None:
                self.right.inorder()

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

    def max(self):
        if not self.data:
         return "Tree is Empty"
        self.max=self.data.value
        def tree(node):
            if node.value>self.max:
                self.max=node.value
            if node.left:
                tree(node.left)
            if node.right:
                tree(node.right)
            return self.max
        return tree(self.data)



if __name__=="main":
 tree = Binary_s_tree(10)
 tree.insert(15)

 tree.insert(20)
 tree.insert(13)
 tree.insert(7)
 tree.insert(4)
 tree.insert(9)


 tree.inorder()
 print()
