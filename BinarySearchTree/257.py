# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rec(self, root, res, direction=[]):
        if not root:
            return
        

        direction.append(str(root.val))
        if not root.left and not root.right:
            res.append("->".join(direction))
        self.rec(root.left, res, direction)
        self.rec(root.right, res, direction)
        direction.pop()
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        
        self.rec(root, res)
        return res