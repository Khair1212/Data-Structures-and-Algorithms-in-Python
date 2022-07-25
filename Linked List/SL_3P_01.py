# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        pt = head

        while pt.next is not None:
            pt.next.next = head
        pt.next = pt.next.next

        head = pt.next

    return head

#         prev = None
#         link = head
#         runner = head

#         while runner is not None:
#             runner = runner.next
#             link.next = prev
#             prev = link
#             link = runner

#         head = prev
#         return head 