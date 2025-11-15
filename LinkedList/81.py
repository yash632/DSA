# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        curr = head.next
        prev = head

        while curr and curr.next:
            if curr.next and curr.val == curr.next.val:
                curr_value = curr.val
                while curr and curr_value == curr.val:
                    curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next


        return dummy.next
            