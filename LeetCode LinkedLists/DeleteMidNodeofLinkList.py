import math


class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def deleteMiddle(self, head):

        if not head or not head.next:
            return None

        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return head


if __name__ == "__main__":

    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(4)
    head.next.next.next = ListNode(7)
    head.next.next.next.next = ListNode(1)
    head.next.next.next.next.next = ListNode(2)
    head.next.next.next.next.next.next = ListNode(6)

    list = []

    solution = Solution()
    new_head = solution.deleteMiddle(head)

    current = new_head
    while current:
        list.append(current.val)
        current = current.next
    print(list)
