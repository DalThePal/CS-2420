'''stack'''

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        '''pushes an item onto the stack'''
        self.stack.append(value)

    def pop(self):
        '''remove the top item from the stack and return it'''
        if len(self.stack) == 0:
            raise IndexError("Stack is empty")

        return self.stack.pop()

    def top(self):
        '''return the top item from the stack without removing it'''
        if len(self.stack) == 0:
            raise IndexError("Stack is Empty")
        return self.stack[len(self.stack) - 1]

    def is_empty(self):
        '''returns true if empty'''
        return len(self.stack) == 0

    def clear(self):
        '''clears the stack'''
        self.stack = []

    def size(self):
        '''return the number of items on the stack'''
        return len(self.stack)
