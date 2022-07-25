"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        curr = head
        while curr:
            # save the curr.next to link later with the copied Node
            nxt = curr.next
            curr.next = Node(curr.val)
            curr.next.next = nxt
            curr = nxt

        # Copy random pointers by just taking the next Node as the next Node refers to the copied Node.
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Separate two parts
        second = cur = head.next
        while cur.next:
            head.next = cur.next
            head = head.next
            cur.next = head.next
            cur = cur.next
        head.next = None
        return second

# Dictionary Approach
#         if not head:
#             return

#         curr, dic = head , {}

#         # create a copy node and save it in a dictionary. So, it will be like dic[old_node] = newNode (copied)
#         while curr:
#             dic[curr] = Node(curr.val)
#             curr = curr.next

#         # Copy the next and the random pointers. Ex: newNode.random =  old_random_pointed_node
#         curr = head
#         while curr:
#             if curr.random:
#                 dic[curr].random = dic[curr.random]
#             if curr.next:
#                 dic[curr].next = dic[curr.next]
#             curr = curr.next
#         return dic[head]

