# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rec(self, root, arr):
        if not root:
            return
        
        arr.append(root.val)
        self.rec(root.left, arr)
        self.rec(root.right, arr)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        self.rec(root, arr)
        return arr