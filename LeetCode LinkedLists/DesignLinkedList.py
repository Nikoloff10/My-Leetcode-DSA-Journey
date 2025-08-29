class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        indexCounter = 0
        while indexCounter < index:
            curr = curr.next
            indexCounter += 1
        return curr.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """

        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """

        node = Node(val)

        if self.head is None:
            self.head = node
        else:
            curr = self.head

            while curr.next is not None:
                curr = curr.next
            curr.next = node
        self.size += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """

        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
            return

        if index == self.size:
            self.addAtTail(val)
            return

        new_node = Node(val)
        curr = self.head
        count = 0

        while count < index - 1:
            curr = curr.next
            count += 1

        new_node.next = curr.next
        curr.next = new_node

        self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """

        if index < 0 or index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        curr = self.head
        count = 0

        while count < index - 1:
            curr = curr.next
            count += 1

        curr.next = curr.next.next
        self.size -= 1


obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1, 2)
obj.get(1)
obj.deleteAtIndex(1)
obj.get(1)
