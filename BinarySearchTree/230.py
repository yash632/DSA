# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def rec(root, k, t, res, flag):
            if not root or flag[0]:
                return
            
            rec(root.left, k, t, res, flag)
            if t[0] == k:
                flag[0] = True
                res[0] = root.val
            t[0] += 1
            rec(root.right, k, t, res, flag)

        res = [0]
        t = [1]
        flag = [False]
        rec(root, k, t, res, flag)
        return res[0]