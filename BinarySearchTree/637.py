from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if self.is_empty():
            return None    
        return self.data.pop(0)

    def peek(self):
        return self.data[0] if not self.is_empty() else None

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)
    
    def display(self):
        print(self.data)

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        if root is None:
            return res
        data = Queue()
        data.enqueue(root)
        
        res.append(root.val)

        while not data.is_empty():
            level = []
            for i in range(data.size()):
                front = data.dequeue()
                if front.left:
                    data.enqueue(front.left)
                    level.append(front.left.val)
                if front.right:
                    data.enqueue(front.right)
                    level.append(front.right.val)
            if level:
                res.append(sum(level)/len(level))
        
        return res