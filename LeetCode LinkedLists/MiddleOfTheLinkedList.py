class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:

    def middleNode(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == "__main__":

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    list = []

    solution = Solution()
    middle_node = solution.middleNode(head)

    while middle_node:
        list.append(middle_node.value)
        middle_node = middle_node.next
    print(list)
