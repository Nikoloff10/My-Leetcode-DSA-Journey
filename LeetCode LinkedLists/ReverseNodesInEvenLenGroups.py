class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def reverseEvenLengthGroups(self, head):
        if not head or not head.next:
            return head

        def _reverse_segment(segment_head, count):
            prev = None
            curr = segment_head
            segment_tail = segment_head

            for _ in range(count):
                if not curr:
                    break
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            return prev, segment_tail, curr

        dummy_head = ListNode(0)
        dummy_head.next = head

        prev_group_tail = dummy_head
        curr = head
        group_num = 1

        while curr:

            group_head = curr
            temp = curr
            actual_group_len = 0

            for _ in range(group_num):
                if not temp:
                    break
                temp = temp.next
                actual_group_len += 1

            if actual_group_len % 2 == 0:

                new_segment_head, new_segment_tail, next_segment_start = _reverse_segment(
                    group_head, actual_group_len)

                prev_group_tail.next = new_segment_head

                new_segment_tail.next = next_segment_start

                prev_group_tail = new_segment_tail
                curr = next_segment_start
            else:
                current_node_in_group = group_head
                for _ in range(actual_group_len):
                    prev_group_tail = current_node_in_group
                    current_node_in_group = current_node_in_group.next
                curr = current_node_in_group

            group_num += 1

        return dummy_head.next


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
    result_value = solution.reverseEvenLengthGroups(head)

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
