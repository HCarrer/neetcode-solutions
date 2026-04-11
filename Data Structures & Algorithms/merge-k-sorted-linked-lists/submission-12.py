# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)

        if n == 0:
            return None

        root = ListNode(0)
        cur = root
        minValues = []

        for lst in lists:
            if lst is not None:
                heapq.heappush(minValues, NodeWrapper(lst))
            
        while minValues:
            node_wrapper = heapq.heappop(minValues)
            cur.next = node_wrapper.node
            cur = cur.next
            if node_wrapper.node.next:
                heapq.heappush(minValues, NodeWrapper(node_wrapper.node.next))

        return root.next





