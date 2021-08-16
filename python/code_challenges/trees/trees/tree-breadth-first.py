class Node:
    def __init__(self ,data):
        self.left = None
        self.right = None
        self.data = data


def breadthfirst(root_value):

    if root_value is None:
        return
    list = []

    list.append(root_value)

    while(len(list) > 0):

        print (list[0].data)
        node = list.pop(0)

        if node.left is not None:
            list.append(node.left)

        if node.right is not None:
            list.append(node.right)
    

root = Node(2)
root.left = Node(7)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(6)
root.right.right = Node(9)
root.left.right.left = Node(5)
root.left.right.right = Node(11)
root.right.right.left = Node(4)

breadthfirst(root)


