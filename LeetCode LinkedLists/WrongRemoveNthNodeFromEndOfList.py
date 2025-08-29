class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def removeNthFromEnd(self, head, n):

        if not head or head is None:
            return head

        curr = head
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        revList = prev
        if n == 1:
            revList = revList.next
            return revList
        count = 1

        temp = revList

        for count in range(n - 2):
            temp = temp.next
            count += 1
        if temp is None or temp.next is None:
            return
        temp.next = temp.next.next

        c = revList
        p = None
        while c:
            n = c.next
            c.next = p
            p = c
            c = n
        result = p
        return result


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
