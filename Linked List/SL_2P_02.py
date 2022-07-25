# Title: Linked List Cycle II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        runner = head
        walker = head
        if head is None:
            return

        while runner is not None and runner.next is not None:
            runner = runner.next.next
            walker = walker.next
            if runner == walker:
                break

        else:
            return

        # Floyd's Cycle Detection
        walker = head
        while walker is not runner:
            walker = walker.next
            runner = runner.next
        return walker

