# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def rec(root, res, arr, t, targetSum):
            if not root:
                return

            res.append(root.val)
            t[0] += root.val
            if not root.left and not root.right:   
                if t[0] == targetSum:
                    arr.append(res.copy())
            rec(root.left, res, arr, t, targetSum)
            rec(root.right, res, arr, t, targetSum)
            res.pop()
            t[0] -= root.val


        res = []
        arr = []
        t = [0]
        rec(root, res, arr, t, targetSum)
        return arr
