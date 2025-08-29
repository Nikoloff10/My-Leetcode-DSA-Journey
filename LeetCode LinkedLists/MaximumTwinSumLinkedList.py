class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """

        n = 0

        stack = []

        curr = head
        max = 0
        while curr:
            n += 1
            stack.append(curr.val)
            curr = curr.next
        for i in range(int(n / 2)):
            num = stack.pop()
            sum = stack[i] + num
            if sum > max:
                max = sum
        return max


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
    result_value = solution.pairSum(head)

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
