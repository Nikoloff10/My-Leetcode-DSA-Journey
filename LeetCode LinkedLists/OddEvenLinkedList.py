class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def oddEvenList(self, head):
        if head is None or head.next is None:
            return head

        odd = head
        even = even_head = head.next

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head


if __name__ == "__main__":
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
    result_value = solution.oddEvenList(head)

    if isinstance(result_value, ListNode):

        result = []
        current = result_value
        while current:
            result.append(current.val)
            current = current.next
        print("Result as list:", result)
    elif isinstance(result_value, int):

        print("Result as integer:", result_value)
    elif result_value is None:

        print("Result: None (empty list)")
    else:

        print("Result:", result_value, "Type:", type(result_value))
