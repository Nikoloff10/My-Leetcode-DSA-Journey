class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def swapNodes(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        curr = ListNode(0)
        curr.next = head
        arr = []
        while curr and curr.next:
            curr = curr.next
            element = curr.val
            arr.append(element)
        vrem = arr[k - 1]
        arr[k - 1] = arr[len(arr) - k]
        arr[len(arr) - k] = vrem
        print(arr)

        values = [x for x in arr]

        if not values:
            head = None
        else:
            head = ListNode(values[0])
            current = head
            for val in values[1:]:
                current.next = ListNode(val)
                current = current.next

        return head


if __name__ == "__main__":
    # Example input: linked list values and n
    values = [
        int(x) for x in input(
            "Enter linked list values separated by spaces: ").split()
    ]
    k = int(input("Enter k: "))

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
    new_head = solution.swapNodes(head, k)

    # Collect result into a list for display
    result = []
    current = new_head
    while current:
        result.append(current.val)
        current = current.next
    print(result)
