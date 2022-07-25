# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        p1 = l1
        p2 = l2
        s = 0
        carry = 0

        while p1 or p2 or carry > 0:
            if p1:
                s += p1.val
                if p1.next is None:
                    last = p1  # Save the last node for next node connection
            if p2:
                s += p2.val
                p2 = p2.next

            if carry:
                s += carry

            carry = int(s / 10)
            if p1:
                p1.val = int(s % 10)
                p1 = p1.next
            else:
                newNode = ListNode(int(s % 10))
                last.next = newNode
                last = last.next
            s = 0
        return l1