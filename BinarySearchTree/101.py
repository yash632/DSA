# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rec(self, a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False

        return (a.val == b.val and self.rec(a.left, b.right) and self.rec(a.right, b.left))

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.rec(root.left, root.right)