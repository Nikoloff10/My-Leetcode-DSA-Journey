class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def removeNthFromEnd(self, head, n):

        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy

        for _ in range(n):
            fast = fast.next
            if not fast and not fast.next:
                return
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return dummy.next


if __name__ == "__main__":
    # Example input: linked list values and n
    values = [
        int(x) for x in input(
            "Enter linked list values separated by spaces: ").split()
    ]
    n = int(input("Enter n (the position from the end to remove): "))

    # Create linked list from input values
    if not values:
        head = None
    else:
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next

    solution = Solution()
    new_head = solution.removeNthFromEnd(head, n)

    # Collect result into a list for display
    result = []
    current = new_head
    while current:
        result.append(current.val)
        current = current.next
    print(result)
