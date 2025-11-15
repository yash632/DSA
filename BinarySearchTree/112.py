# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def rec(self, root, result, targetSum, res=[0]):
        if not root or result[0]:
            return

        res[0] += root.val
        if not root.left and not root.right:
            if res[0] == targetSum:
                result[0] = True
        self.rec(root.left, result, targetSum, res)
        self.rec(root.right, result, targetSum, res)
        res[0] -= root.val

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        result = [False]

        self.rec(root, result, targetSum)
        return result[0]
        
    