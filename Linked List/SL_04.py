# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return

        curr = head
        size = 0

        # get the size and preserve the last Node
        while curr:
            if not curr.next:
                last = curr
            curr = curr.next
            size += 1

        # steps to rotate
        k = k % size

        # Calculate how many steps to move
        move = size - k

        # Move from the head again
        curr = head
        for i in range(move - 1):
            curr = curr.next

        # Break the Node connection and make new connection to rotate
        last.next = head
        head = curr.next
        curr.next = None
        return head

