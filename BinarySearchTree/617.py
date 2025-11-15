# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rec(self, a, b, dummy):
        if not a and not b:
            return
        if not a:
            dummy.val = b.val
        if not b:
            dummy.val = a.val
        else:
            dummy.val = a.val + b.val

        self.rec(a.left, b.left, dummy.left)
        self.rec(a.right, b.right, dummy.right)
        
    def mergeTrees(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> Optional[TreeNode]:
        if not a and not b:
            return

        root = TreeNode((a.val if a else 0) + (b.val if b else 0))
        root.left = self.mergeTrees((a.left if a else None), (b.left if b else None))
        root.right = self.mergeTrees((a.right if a else None), (b.right if b else None))
        return root