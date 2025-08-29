# def reverse_list(head):
#     prev = None
#     curr = head
#     while curr:
#         next_node = curr.next # first, make sure we don't lose the next node
#         curr.next = prev      # reverse the direction of the pointer
#         prev = curr           # set the current node to prev for the next node
#         curr = next_node      # move on

#     return prev


class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def reverseBetween(self, head, left, right):

        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        current = prev.next
        for _ in range(right - left):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next


if __name__ == "__main__":

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    left = 1
    right = 5

    list = []

    solution = Solution()
    new_head = solution.reverseBetween(head, left, right)

    current = new_head
    while current:
        list.append(current.val)
        current = current.next
    print(list)
