class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def print_pre_order(self):

        stack = ""
        if not self.root:
            return 'empty tree'

        def traverse(node):
            stack = str(node.value)

            if node.left:
                traverse(node.left)

            if node.right:
                traverse(node.right)

        traverse(self.root)

        return stack



if __name__ == "__main__":

    p = BinaryTree()
    p.print_pre_order()















