class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -1 * nums[i]

        heapq.heapify(nums)

        element = 0
        while k > 0:
            element = heapq.heappop(nums)
            k-=1

        return -1 * element