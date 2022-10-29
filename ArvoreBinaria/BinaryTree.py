from typing import Any
from enum import Enum


class Node:
    def __init__(self, content: Any) -> None:
        self.content = content
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(self.content)


class Origin(Enum):
    ROOT = 1
    CURSOR = 2


class BinaryTree:
    def __init__(self, root_content: Any = None) -> None:
        self.__root = Node(
            root_content) if root_content is not None else root_content
        self.__cursor = self.__root  # cursor starts at tree's root

    def createRoot(self, root_content: Any):
        if self.__root is None:
            self.__root = Node(root_content)

    def isEmpty(self) -> bool:
        return self.__root is not None
        # it's the same as 'return self.__root == None

    def getRoot(self) -> Any:
        # if self.__root is not None, there is a Node in it
        return self.__root.content if self.__root is not None else None

    def getCursor(self) -> Any:
        return self.__cursor.content if self.__cursor is not None else None

    def preorder(self, origin: Origin = Origin.ROOT):
        if origin == Origin.ROOT:
            self.__preorder(self.__root)
        elif origin == Origin.CURSOR:
            self.__preorder(self.__cursor)

    def __preorder(self, node):
        if node is None:
            return
        print(f'{node.content}', end=' ')
        self.__preorder(node.left)
        self.__preorder(node.right)

    def inorder(self):
        self.__inorder(self.__root)

    def __inorder(self, node):
        if node is None:
            return
        self.__inorder(node.left)
        print(f'{node.content}', end=' ')
        self.__inorder(node.right)

    def postorder(self):
        self.__postroder(self.__root)

    def __postorder(self, node):
        if node is None:
            return
        self.__postorder(node.left)
        self.__postorder(node.right)
        print(f'{node.content}', end=' ')

    def goDownLeft(self):
        if self.__cursor is not None and \
           self.__cursor.left is not None:
            self.__cursor = self.__cursor.left

    def goDownRight(self):
        if self.__cursor is not None and \
           self.__cursor.right is not None:
            self.__cursor = self.__cursor.right

    def resetCursor(self):
        self.__cursor = self.__root

    def addLeftChild(self, content: Any) -> bool:
        if self.__cursor is not None:
            if self.__cursor.left is None:
                self.__cursor.left = Node(content)
                return True
        else:
            return False

    def addRightChild(self, content: Any) -> bool:
        if self.__cursor is not None:
            if self.__cursor.right is None:
                self.__cursor.right = Node(content)
                return True
        else:
            return False

    def height(self) -> int:
        return self.__height(self.__root)

    def __height(self, node) -> int:
        if node is None:
            return 0

    def __count(self, node: Node) -> int:

        if node is None:
            return 0
        return 1 + self.__count(node.left) + self.__count(node.right)

    def __len__(self):
        return self.__count(self.__root)

    def search(self, key, node):
        return self.__search(key, self.__root)

    def __search(self, key, node: Node):
        if node is None:
            return False
        if node.content == key:
            return True
        if self.__search(key, node.left):
            return True
        else:
            return self.__search(key, node.right)

    def removeNode(self, key: Any):
        if self.__cursor is None:
            return
        # Checks if the key is on the left or on the right of the cursor
        if self.__cursor.left is not None and self.__cursor.left.content == key:
            # Checking if the node is a leaf
            if self.__cursor.left.left == None and \
                    self.__cursor.left.right == None:
                self.__cursor.left = None
        elif self.__cursor.right is not None and self.__cursor.right.content == key:
            if self.__cursor.right.left == None and \
                    self.__cursor.right.right == None:
                self.__cursor.right = None

    # TODO - explain to myself how does '__go' works
    def go(self, key: int) -> Node:
        return self.__go(key, self.__root)

    def __go(self, key: int, node: Node) -> Node:
        if node is None:
            return None
        if node.content == key:
            return node
        result = self.__go(key, node.left)
        if result:
            return result
        else:
            return self.__go(key, node.right)

    def removeRoot(self) -> bool:
        '''It only removes the root if the tree has only the root'''
        if len(self) == 1:
            self.__root = self.__cursor = None
            return True
        else:
            return False
