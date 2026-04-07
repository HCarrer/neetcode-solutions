# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = head
        cur = head.next
        while cur:
            print(cur.val, cur.val)
            if cur.val >= prev.val:
                prev, cur = cur, cur.next
                continue
            

            tmp = dummy
            while cur.val > tmp.next.val:
                tmp = tmp.next

            prev.next = cur.next
            cur.next = tmp.next
            tmp.next = cur
            cur = prev.next

        return dummy.next