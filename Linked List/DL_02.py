"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        walker = head
        stack = []
        while walker:
            if walker.child:
                if walker.next:
                    stack.append(walker.next)
                walker.next = walker.child
                walker.child.prev = walker
                walker.child = None

            if not walker.next:
                if not stack:
                    break
                top_node = stack.pop()
                walker.next = top_node
                top_node.prev = walker
            walker = walker.next
        return head
