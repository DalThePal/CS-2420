'''main'''
from binarysearchtree import BinarySearchTree

def main():
    '''main'''

    data = [21, 26, 30, 9, 4, 14, 28, 18, 15, 10, 2, 3, 7]
    remove_data = [21, 9, 4, 18, 15, 7]

    tree = BinarySearchTree()
    for i in range(511):
        tree.add(i)

    tree.rebalance_tree()



if __name__ == "__main__":
    main()
