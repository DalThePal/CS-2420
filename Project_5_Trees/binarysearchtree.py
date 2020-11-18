'''binarysearchtree module'''

from recursioncounter import RecursionCounter

class Node:
    '''Node class to be used with Binary Search Tree'''

    def __init__(self, data, left_child=None, right_child=None):
        '''initializes the class'''
        self.data = data
        self.left_child = left_child
        self.right_child = right_child
        self.height = 0

    def is_leaf(self):
        '''returns True if node doesnt have children'''
        return self.left_child is None and self.right_child is None

    def update_height(self):
        '''updates the height'''
        if  self.is_leaf():
            self.height = 0

        elif self.left_child is not None and self.right_child is None:
            self.height = self.left_child.update_height() + 1

        elif self.right_child is not None and self.left_child is None:
            self.height = self.right_child.update_height() + 1

        else:
            self.height = max(self.left_child.update_height() + 1, self.right_child.update_height() + 1)

        return self.height

    def get_height(self):
        '''returns the node's height'''
        return self.height

    def __str__(self):
        '''returns the nodes data in a string'''
        data = str(self.data)
        height = ' ({0})'.format(self.get_height())
        leaf = ''

        if self.is_leaf():
            leaf = ' [leaf]'
        return data + height + leaf + '\n'

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
        if self.root is None:
            return 0
        else:
            return 1 + self.__len_helper(self.root.left_child) + self.__len_helper(self.root.right_child)

    def __len_helper(self, cursor):
        '''recursion helper for self.__len__'''
        RecursionCounter()

        if cursor is None:
            return 0

        else:
            return 1 + self.__len_helper(cursor.left_child) + self.__len_helper(cursor.right_child)

    def height(self):
        '''return the height of the tree'''
        self.root.update_height()
        return self.root.get_height()

    def __str__(self):
        '''return a string that shows the shape of the three when printed'''
        return self.__str_helper(self.root)

    def __str_helper(self, cursor, tab_count=0):
        '''recursion helper for self.__str__'''
        RecursionCounter()
        tabs = "\t" * (tab_count)

        if cursor is None:
            return tabs + '[Empty] \n'

        elif cursor.is_leaf():
            return tabs + str(cursor)

        else:
            tab_count += 1
            return tabs + str(cursor) + self.__str_helper(cursor.left_child, tab_count) + self.__str_helper(cursor.right_child, tab_count)

    def add(self, data):
        '''add item to its proper place in the tree'''
        if isinstance(data, list):
            for item in data:
                self.root = self.__add_helper(self.root, item)

        else:
            self.root = self.__add_helper(self.root, data)

        self.root.update_height()

    def __add_helper(self, cursor, item):
        '''recursion helper for self.add'''
        RecursionCounter()

        if cursor is None:
            return Node(item)

        elif cursor.data < item:
            cursor.right_child = self.__add_helper(cursor.right_child, item)

        elif cursor.data > item:
            cursor.left_child = self.__add_helper(cursor.left_child, item)

        return cursor

    def remove(self, data):
        '''remove item from the tree'''
        if isinstance(data, list):
            for item in data:
                self.__remove_helper(self.root, item)

        else:
            self.__remove_helper(self.root, data)

        if self.root is not None:
            self.root.update_height()

    def __remove_helper(self, cursor, item):
        '''recursion helper for self.remove'''
        RecursionCounter()

        if cursor is None:
            return None

        elif item < cursor.data:
            cursor.left_child = self.__remove_helper(cursor.left_child, item)
        elif item > cursor.data:
            cursor.right_child = self.__remove_helper(cursor.right_child, item)

        else:
            if cursor.is_leaf():
                cursor = None

            elif cursor.left_child is not None and cursor.right_child is not None:
                cursor.data = self.__min_value(cursor.right_child)
                cursor.right_child = self.__remove_helper(cursor.right_child, cursor.data)

            elif cursor.left_child is None and cursor.right_child is not None:
                cursor = cursor.right_child

            elif cursor.right_child is None and cursor.left_child is not None:
                cursor = cursor.left_child

        return cursor

    def __min_value(self, item):
        """Finds the min value in the tree."""
        if item.left_child is None:
            return item.data
        else:
            return self.__min_value(item.left_child)

    def find(self, item):
        '''return the matched item.  if item is not in the tree, return None'''
        return self.__find_helper(self.root, item)

    def __find_helper(self, cursor, item):
        '''recursion helper for self.find'''
        RecursionCounter()

        if cursor is None:
            return None

        elif cursor.is_leaf():
            return None

        elif item > cursor.data:
            return self.__find_helper(cursor.right_child, item)

        elif item < cursor.data:
            return self.__find_helper(cursor.left_child, item)

        elif item == cursor.data:
            return cursor

    def preorder(self):
        '''return an iterator that preforms an inorder traversal of the tree'''
        lyst = []
        self.__preorder_helper(self.root, lyst)
        return lyst

    def __preorder_helper(self, cursor, lyst):
        '''recursion helper for self.preorder'''
        RecursionCounter()

        if cursor is not None:
            lyst.append(cursor.data)
            self.__preorder_helper(cursor.left_child, lyst)
            self.__preorder_helper(cursor.right_child, lyst)
