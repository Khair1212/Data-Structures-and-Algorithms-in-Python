# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        walker = head
        runner = head

        # Get the Middle
        while runner and runner.next:
            if runner.next.next is None:
                break
            runner = runner.next.next
            walker = walker.next

        # Walker refers to the end node of the first half
        # Assign a new variable here to start the second half
        # if linked list size is odd take the next walker node otherwise the current walker node
        if runner.next is not None:
            head_2 = walker.next
        else:
            head_2 = walker

        # Reverse the second half
        pointer = head_2
        prev = None
        runner = head_2.next

        while runner is not None:
            pointer.next = prev
            prev = pointer
            pointer = runner
            runner = runner.next
        # link the last node
        pointer.next = prev
        head_2 = pointer

        # Check first Half with the Second Half
        while head is not walker.next:
            if (head.val != head_2.val):
                return False
            head = head.next
            head_2 = head_2.next

        return True



