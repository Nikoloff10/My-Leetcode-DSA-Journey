class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        current = head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while current and current.next:

            if current.val == current.next.val:
                dupe_val = current.val
                while current and current.val == dupe_val:
                    current = current.next

                prev.next = current
            else:
                prev = prev.next
                current = current.next

        return head


if __name__ == "__main__":
    # Example input: linked list values and n
    values = [
        int(x) for x in input(
            "Enter linked list values separated by spaces: ").split()
    ]

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
    new_head = solution.deleteDuplicates(head)

    # Collect result into a list for display
    result = []
    current = new_head
    while current:
        result.append(current.val)
        current = current.next
    print(result)
