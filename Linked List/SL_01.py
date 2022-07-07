# Title: Design Linked List

class Node(object):
    def __init__(self, data=None):
        self.value = data
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:

        if index < 0 or index >= self.size:
            return -1
        if self.head is None:
            return -1

        iterator = self.head
        for i in range(index):
            iterator = iterator.next
        return iterator.value

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        iterator = self.head
        if iterator is None:
            self.addAtHead(val)
        else:
            while iterator.next is not None:
                iterator = iterator.next
            iterator.next = newNode
            self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = Node(val)
        iterator = self.head

        if index < 0 or index > self.size:
            return

        # check head
        if index == 0:
            self.addAtHead(val)
        else:
            for i in range(index - 1):
                iterator = iterator.next

            newNode.next = iterator.next
            iterator.next = newNode
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:

        if index < 0 or index >= self.size:
            return
        iterator = self.head

        # head checking
        if index == 0:
            self.head = iterator.next
        else:
            # remove between and last

            for i in range(index - 1):
                iterator = iterator.next

            iterator.next = iterator.next.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)