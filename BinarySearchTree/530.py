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
        self.rec(root.left, res)
        res.append(root.val)
        self.rec(root.right, res)
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        res = []
        self.rec(root, res)
            
        return min(b - a for a, b in zip(res, res[1:]))

        