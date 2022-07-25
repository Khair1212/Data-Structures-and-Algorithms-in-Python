# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        runner = head
        walker = head
        count = 0

        try:
            for i in range(n):
                runner = runner.next
        except:
            return

        if runner is None:
            return head.next
        else:
            while runner.next is not None:
                runner = runner.next
                walker = walker.next

        walker.next = walker.next.next
        return head


