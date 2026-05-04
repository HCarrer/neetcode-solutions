class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float("inf")

        for r in range(len(nums)):
            currentSum = nums[r]
            l = r
            while l > 0 and currentSum < target:
                l -= 1
                currentSum += nums[l]

            if currentSum >= target:
                minLen = min(minLen, r-l+1)

        return minLen if minLen <= len(nums) else 0