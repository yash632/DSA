# Definition for a binary tree node.
from math import inf
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def rec(root, l, h):
            if not root:
                return True

            if not(l < root.val < h):
                return False
            
            return rec(root.left, l, root.val) and rec(root.right, root.val, h)

        return rec(root, (-inf), (inf))