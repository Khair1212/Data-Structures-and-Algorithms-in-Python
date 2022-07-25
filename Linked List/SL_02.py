# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        def insert(head, index, val):
            runner = head
            newNode = ListNode(val=val)
            if index == 0:
                newNode.next = head
                head = newNode
                return head

            for i in range(index - 1):
                if (runner is None):
                    return
                runner = runner.next
            newNode.next = runner.next
            runner.next = newNode
            return head

        left = list1
        right = list2

        index = 0
        while True:
            if left is None or right is None:
                break
            if left.val <= right.val:
                left = left.next
            else:
                list1 = insert(list1, index, right.val)
                right = right.next

            index += 1

        while (right is not None):
            list1 = insert(list1, index, right.val)
            right = right.next
            index += 1

        return list1