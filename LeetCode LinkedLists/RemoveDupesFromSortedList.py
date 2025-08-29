class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def deleteDuplicates(self, head):

        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head


# Example usage:
if __name__ == "__main__":

    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)

    list = []

    solution = Solution()
    new_head = solution.deleteDuplicates(head)

    current = new_head
    while current:
        list.append(current.val)
        current = current.next
    print(list)
