# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], v: int) -> Optional[TreeNode]:
        def rec(root, v):
            if not root:
                return 

            if v < root.val:
                rec(root.left, v)
            if v > root.val:
                rec(root.right, v)
            if v < root.val and not root.left:
                root.left = TreeNode(v)
            if v > root.val and not root.right:
                root.right = TreeNode(v)
        if not root:
            root = TreeNode(v)
        rec(root, v)
        return root