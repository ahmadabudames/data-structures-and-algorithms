
from trees.trees import *

def test_instantiate_empty_tree():
 tree = Binary_s_tree()

 assert tree.data==None


def test_single_root():
 tree = Binary_s_tree(10)

 assert tree.data==10

def test_left_right_single_root():
 tree = Binary_s_tree(10)
 tree.insert(7)
 tree.insert(15)

 assert tree.data==10
 assert tree.right.data==15
 assert tree.left.data==7


def test_preorder():
 tree = Binary_s_tree(10)
 tree.insert(14)
 tree.insert(17)
 tree.insert(11)
 tree.insert(7)
 tree.insert(4)
 tree.insert(9)

 assert tree.preorder() =='10-->7-->4-->9-->14-->11-->17-->'

def test_inorder():
 tree = Binary_s_tree(10)
 tree.insert(14)
 tree.insert(17)
 tree.insert(11)
 tree.insert(7)
 tree.insert(4)
 tree.insert(9)

 assert tree.inorder() =='4-->7-->9-->10-->11-->14-->17-->'

def test_postorder():
 tree = Binary_s_tree(10)
 tree.insert(14)
 tree.insert(17)
 tree.insert(11)
 tree.insert(7)
 tree.insert(4)
 tree.insert(9)

 assert tree.inorder() =='4-->9-->7-->10-->11-->17-->14-->'
