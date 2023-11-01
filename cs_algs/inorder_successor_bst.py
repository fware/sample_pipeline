from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return None

    stack = []
    ans = []
    while True:
        while root:
            stack += [root]
            root = root.left
        if not stack:
            return ans
        curr = stack.pop()
        ans += [curr.val]
        root = curr.right

    return ans


root = TreeNode(1)
