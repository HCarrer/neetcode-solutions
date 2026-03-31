class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        maxNums = []
        
        for r in range(k, len(nums)+1):
            hash = nums[l:r]
            maxNums.append(max(hash))
            l+=1
        return maxNums