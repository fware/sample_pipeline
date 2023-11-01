# Python3 program to for tree traversals


# A class that represents an individual node in a
# Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A function to do inorder tree traversal
def print_inorder(root_l):
    if root_l:
        # First recur on left child
        print_inorder(root_l.left)

        # Then print the data of node
        print(root_l.val, end=" "),

        # Now recur on right child
        print_inorder(root_l.right)


# Driver code
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    # Function call
    print("Inorder traversal of binary tree is")
    print_inorder(root)
