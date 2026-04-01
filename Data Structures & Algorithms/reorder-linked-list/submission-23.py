# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # head                      [2,4,6,8]
        # find middle               [2,4,6,8]
        # reverse second half       [2,4,8,6] kinda like [[2,4],[8,6]]
        # rewrite                   [2,8,4,6]

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow.next
        slow.next = None # splitting the list
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # [2,4,8,6]
        # leftHalf aponta pra 2 e rightHalf aponta pra 8
        leftHalf, rightHalf = head, prev
        while rightHalf:
            tmp1 = leftHalf.next # tmp1 aponta pra 4
            tmp2 = rightHalf.next # tmp2 aponta pra 6
            leftHalf.next = rightHalf # leftHalf (2) aponta pra 8
            rightHalf.next = tmp1  # rightHalf (8) aponta pra 4
            leftHalf = tmp1 # leftHalf aponta pra 4
            rightHalf = tmp2 # rightHalf aponta pra 6
