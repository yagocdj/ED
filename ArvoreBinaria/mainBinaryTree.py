#!usr/bin python3
from BinaryTree import BinaryTree

# Lista 10.1
# Q1

# Test case 1
""" b_tree = BinaryTree(1)
b_tree.addLeftChild(2)
b_tree.addRightChild(3)
b_tree.goDownLeft()
b_tree.addRightChild(4)

b_tree.resetCursor()

b_tree.goDownRight()
b_tree.addLeftChild(5)
b_tree.addRightChild(6)
b_tree.goDownRight()
b_tree.addLeftChild(7) """


""" # Test case 2
b_tree = BinaryTree('A')  # root is 'A'
b_tree.addLeftChild('B')
b_tree.addRightChild('C')
b_tree.goDownLeft()
b_tree.addRightChild('D')

b_tree.resetCursor()

b_tree.goDownRight()
b_tree.addRightChild('E')
b_tree.goDownRight()
b_tree.addLeftChild('F')
b_tree.addRightChild('G')
b_tree.goDownRight()
b_tree.addLeftChild('H')
 """
# Test case 3
b_tree = BinaryTree(1)
b_tree.addLeftChild(2)

b_tree.preorder()  # default is root
print()

print('Quantidade de nós folha:', b_tree.leafsCount())
print('Altura da árvore:', b_tree.height())
