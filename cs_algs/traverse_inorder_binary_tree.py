# Python3 program to populate
# inorder traversal of all nodes

# Tree node


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None


# The first visited node will be
# the rightmost node next of the
# rightmost node will be None
next = None


# Set next of p and all descendants of p
# by traversing them in reverse Inorder


def populateNext(p):
    global next

    if (p != None):
        # First set the next pointer
        # in right subtree
        populateNext(p.right)

        # Set the next as previously visited node
        # in reverse Inorder
        p.next = next

        # Change the prev for subsequent node
        next = p

        # Finally, set the next pointer
        # in left subtree
        populateNext(p.left)


# UTILITY FUNCTIONS
# Helper function that allocates
# a new node with the given data
# and None left and right pointers.


def newnode(data):
    node = Node(0)
    node.data = data
    node.left = None
    node.right = None
    node.next = None

    return node


# Driver Code


# Constructed binary tree is
#	  10
#	 / \
#   8   12
#  /
# 3
root = newnode(10)
root.left = newnode(8)
root.right = newnode(12)
root.left.left = newnode(3)

# Populates nextRight pointer
# in all nodes
p = populateNext(root)

# Let us see the populated values
ptr = root.left.left
while (ptr != None):

    out = 0
    if (ptr.next != None):
        out = ptr.next.data
    else:
        out = -1

    # -1 is printed if there is no successor
    print("Next of", ptr.data, "is", out)
    ptr = ptr.next

# This code is contributed by Arnab Kundu
