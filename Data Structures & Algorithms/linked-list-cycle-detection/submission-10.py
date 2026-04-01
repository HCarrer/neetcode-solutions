# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 
        # O(n) approach for time and memory
        # 
        # visitedNodes = set()
        # while head:
        #     if head in visitedNodes:
        #         return True
        #     visitedNodes.add(head)
        #     head = head.next

        # return False

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
