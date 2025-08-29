class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def getDecimalValue(self, head):

        values = []
        sum = 0

        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        while curr.next:
            curr = curr.next
            values.append(curr.val)

        values.reverse()
        for i in range(len(values)):
            num = 2**i * values[i]
            sum += num

        return sum


if __name__ == "__main__":
    values = [
        int(x) for x in input(
            "Enter linked list values separated by spaces: ").split()
    ]

    if not values:
        head = None
    else:
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next

    solution = Solution()
    result_value = solution.getDecimalValue(head)

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
