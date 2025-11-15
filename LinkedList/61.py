# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        if head == None:
            return head

        n = 1
        while curr.next:
            curr = curr.next
            n += 1

        curr.next = head
        if k >= n:
            k = k % n

        for i in range((n - k) - 1):
            head = head.next
        temp = head.next
        head.next = None
        head = temp
        
        return head
