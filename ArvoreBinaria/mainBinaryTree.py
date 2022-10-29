#!usr/bin python3
from BinaryTree import BinaryTree

# Lista 10.1
# Q1

""" b_tree = BinaryTree(1)
b_tree.addLeftChild(2)
b_tree.addRightChild(3)
b_tree.goDownLeft()
b_tree.addRightChild(4)

b_tree.resetCursor()

b_tree.goDownRight()
b_tree.addLeftChild(5)
b_tree.addRightChild(6) """

b_tree = BinaryTree('A')

b_tree.addRightChild('B')

b_tree.preorder()  # default is root
print()

print(b_tree.leafsCount())
