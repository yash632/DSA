# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def rec(root, res, arr):
            if not root:
                return
            
            arr.append(str(root.val))
            if not root.left and not root.right:
                res.append(int("".join(arr)))
            rec(root.left, res, arr)
            rec(root.right, res, arr)
            arr.pop()

        res = []
        arr = []
        rec(root, res, arr)
        print(res)
        return sum(res)
        