from statistics import mode
from collections import Counter
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
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        self.rec(root, res)

        count = Counter(res)
        freq = max(count.values())
        res = []
        for i in count:
            if count[i] == freq:
                res.append(i)            
        return res