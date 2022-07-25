# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        #         p1 = headA

        #         while p1 is not None:
        #             p2 = headB
        #             while p2 is not None:
        #                 if p1 == p2:
        #                     return p1
        #                 p2 = p2.next
        #             p1 = p1.next

        p1 = headA
        p2 = headB

        while (p1 != p2):

            if p1 is None:
                p1 = headB
            else:
                p1 = p1.next

            if p2 is None:
                p2 = headA
            else:
                p2 = p2.next

        return p1

#         Dictionary Solution
#         d = {}

#         while headA is not None:
#             d[headA] = 1
#             headA = headA.next

#         while headB is not None:
#             if headB in d.keys():
#                 return headB
#             headB = headB.next

