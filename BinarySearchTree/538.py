# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def rec(root, t):
            if not root:
                return
            
            rec(root.right, t)
            t[0] += root.val
            root.val = t[0]
            rec(root.left, t)
        
        t = [0]
        rec(root, t)
        return root
