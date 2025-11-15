# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rec(self, root, res):
        if not root:
            return
    
        if root.left:
            if not root.left.left and not root.left.right:    
                res[0] += root.left.val
        self.rec(root.left, res)
        self.rec(root.right, res)
        
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = [0]
        
        self.rec(root, res)
        return res[0]        