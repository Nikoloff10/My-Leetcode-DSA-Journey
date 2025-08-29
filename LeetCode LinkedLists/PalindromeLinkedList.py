class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """

        dummy = ListNode(0)
        current_copy = dummy

        curr_org = head

        result = False

        while curr_org:
            new_node = ListNode(curr_org.val)
            current_copy.next = new_node
            current_copy = current_copy.next
            curr_org = curr_org.next

        prev = None
        curr = dummy.next
        while curr:
            vrem = curr.next
            curr.next = prev
            prev = curr
            curr = vrem

        norm = head
        rev = prev
        failsCount = 0
        while norm and rev:
            if norm.val == rev.val:
                result = True
            else:
                failsCount += 1
                if failsCount >= 1:
                    result = False
                    return result
            norm = norm.next
            rev = rev.next
        return result


if __name__ == "__main__":
    # Example input: linked list values
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
    is_palindrome = solution.isPalindrome(head)
    print("Is palindrome:", is_palindrome)
