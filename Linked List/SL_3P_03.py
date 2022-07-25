# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return

        pointer = head
        prev = head
        runner = head.next
        count = 2

        while runner is not None:
            if count % 2 != 0:
                prev.next = runner.next
                runner.next = pointer.next
                pointer.next = runner
                pointer = runner
                runner = prev.next
            else:
                prev = runner
                runner = runner.next
            count += 1

        return head