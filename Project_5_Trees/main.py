'''main'''
from binarysearchtree import BinarySearchTree

def main():
    '''main'''

    data = [21, 26, 30, 9, 4, 14, 28, 18, 15, 10, 2, 3, 7]
    remove_data = [21, 9, 4, 18, 15, 7]

    tree = BinarySearchTree()
    tree.add(data)

    print(str(tree.preorder())[1:-1])
    print(tree)

    tree.remove(remove_data)

    print(tree)

if __name__ == "__main__":
    main()
