'''binarysearchtree module'''

from recursioncounter import RecursionCounter

class Node:
    '''Node class to be used with Binary Search Tree'''

    def __init__(self, data, left_child=None, right_child=None):
        '''initializes the class'''
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

    def is_leaf(self):
        '''returns True if node is a leaf in the binary tree'''
        return self.left_child is None and self.right_child is None

    def update_height(self):
        '''updates the height'''
        if  self.is_leaf():
            return 0

        elif self.left_child is not None and self.right_child is None:
            return self.left_child.update_height() + 1

        elif self.right_child is not None and self.left_child is None:
            return self.right_child.update_height() + 1

        else:
            self.height = max(self.left_child.update_height(), self.right_child.update_height())

        return self.height

    def get_height(self):
        '''returns the node's height'''
        return self.height

    def __str__(self):
        '''returns the nodes data in a string'''
        return str(self.data)

class BinarySearchTree:
    '''Binary Search Tree ADT'''

    def __init__(self):
        '''initializes the class'''
        self.root = None

    def is_empty(self):
        '''return True if empty, False otherwise'''
        return self.root is None

    def __len__(self):
        '''return the umber of items in the tree'''
        return

    def height(self):
        '''return the height of the tree'''
        self.root.update_height()
        return self.root.get_height()

    def __str__(self):
        '''return a string that shows the shape of the three when printed'''
        return

    def add(self, item):
        '''add item to its proper place in the tree'''
        self.root = self.__add_helper(self.root, item)
        self.root.update_height()

    def __add_helper(self, cursor, item):
        '''recursion helper for self.add'''
        RecursionCounter()

        if cursor is None:
            return None

        elif cursor.data < item:
            cursor.right_child = self.__add_helper(cursor.right_child, item)

        else:
            cursor.left_child = self.__add_helper(cursor.left_child, item)

        return cursor

    def remove(self, item):
        '''remove item from the tree'''
        self.root = self.__remove_helper(self.root, item)

    def __remove_helper(self, cursor, item):
        '''recursion helper for self.remove'''
        RecursionCounter()
        return

    def find(self, item):
        '''return the matched item.  if item is not in the tree, return None'''
        return

    def __find_helper(self, cursor, item):
        '''recursion helper for self.find'''
        RecursionCounter()
        return

    def preorder(self):
        '''return an iterator that preforms an inorder traversal of the tree'''
        return

    def __preorder_helper(self, cursor, output):
        '''recursion helper for self.preorder'''
        RecursionCounter()
        return
