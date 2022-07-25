# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        def removeNode(head, value):
            if head is None:
                return head

            while (head.val == value):
                head = head.next
                if head is None:
                    return head

            runner = head

            while (runner.next is not None):
                if runner.next.val == value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next

            return head

        return removeNode(head, val)
