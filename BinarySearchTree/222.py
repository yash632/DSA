# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rec(self, root, res):
        if not root:
            return 
        
        res[0] += 1
        self.rec(root.left, res)
        self.rec(root.right, res)
    def countNodes(self, root: Optional[TreeNode]) -> int:
        res = [0]

        self.rec(root, res)
        return res[0]