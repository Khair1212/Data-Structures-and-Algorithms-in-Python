# Title: Linked List Cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        walker = head
        runner = head
        if head is None:
            return False
        while runner.next is not None and runner.next.next is not None:
            runner = runner.next.next
            walker = walker.next
            if walker == runner:
                return True
        return False
