from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the list is empty or has only one node, return it as is
        if not head or not head.next:
            return head
        
        current = head
        
        # Traverse the list
        while current and current.next:
            # If current node's value equals the next node's value
            if current.val == current.next.val:
                # Skip the next node by updating the next pointer
                current.next = current.next.next
            else:
                # Move to the next node only if no duplicate was found
                current = current.next
                
        return head