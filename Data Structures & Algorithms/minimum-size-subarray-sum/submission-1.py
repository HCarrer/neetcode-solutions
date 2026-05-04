class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float("inf")
        l, total = 0, 0

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                minLen = min(minLen, r-l+1)
                total -= nums[l]
                l += 1

        return minLen if minLen <= len(nums) else 0