from tree_intersection.hashMap import *


class Node:
    def __init__(self, data):
        self.data = data
        self.l = None
        self.R = None



class tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.l is not None:
                self._insert(data, node.l)
            else:
                node.l = Node(data)
        else:
            if node.R is not None:
                self._insert(data, node.R)
            else:
                node.R = Node(data)


def intersection(firstTree,secondTree):
    list=[]
    hashtree=HashTable(720)

    if firstTree.root==None or secondTree.root==None:
        return None

    def travers(node):
        if hashtree.contains(str(node.data)):
            nonlocal list
            list+=[node.data]
        else:
            hashtree.add(str(node.data),True)

        if node.l:
            travers(node.l)
        if node.R:
            travers(node.R)
    travers(firstTree.root)
    travers(secondTree.root)

    return list



if __name__ == "__main__":

    firstTree = tree()
    firstTree.insert(100)
    firstTree.insert(90)
    firstTree.insert(300)
    firstTree.insert(20)
    firstTree.insert(200)


    secondTree = tree()

    secondTree.insert(100)
    secondTree.insert(200)
    secondTree.insert(160)
    secondTree.insert(300)
    secondTree.insert(30)

    print(intersection(firstTree , secondTree))
