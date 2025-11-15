# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        d = deque()
        d.append(root)

        depth = 0
        while d:
            depth += 1
            for _ in range(len(d)):
                front = d.popleft()
                if front.left is None and front.right is None:
                    return depth
                if front.left:
                    d.append(front.left)
                if front.right:
                    d.append(front.right)

        return depth
                    
                  