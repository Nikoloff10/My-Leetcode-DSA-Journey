class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(0)
        dummy.next = head
        curr = dummy

        while curr.next:

            if val == curr.next.val:

                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next


if __name__ == "__main__":
    values = [
        int(x) for x in input(
            "Enter linked list values separated by spaces: ").split()
    ]
    vall = int(input("Enter value to remove: "))

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
    result_value = solution.removeElements(head, vall)

    # Check the type of the returned value and handle accordingly
    if isinstance(result_value, ListNode):
        # If it's a ListNode, traverse and collect values
        result = []
        current = result_value
        while current:
            result.append(current.val)
            current = current.next
        print("Result as list:", result)
    elif isinstance(result_value, int):
        # If it's an integer, print it directly
        print("Result as integer:", result_value)
    elif result_value is None:
        # Handle None case
        print("Result: None (empty list)")
    else:
        # Handle any other unexpected types
        print("Result:", result_value, "Type:", type(result_value))
