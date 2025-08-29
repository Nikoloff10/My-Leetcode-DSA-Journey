class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseList(self, head):

        prev = None
        curr = head

        while curr:

            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev


if __name__ == "__main__":

    head = ListNode(0)
    # head.next = ListNode(1)
    # head.next.next = ListNode(2)
    # head.next.next.next = ListNode(3)
    # head.next.next.next.next = ListNode(4)

    list = []

    solution = Solution()
    new_head = solution.reverseList(head)

    current = new_head
    while current:
        list.append(current.val)
        current = current.next
    print(list)
