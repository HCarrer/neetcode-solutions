class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        longest = 0
        r=0

        for l in range(len(nums)):
            while r<len(nums) and (nums[r] - nums[l] <= limit):
                biggest, smallest = max(nums[l:r+1]), min(nums[l:r+1])
                maxDiff = abs(biggest - smallest)
                if maxDiff <= limit:
                    longest = max(longest, r-l+1)
                r+=1
            r=l+1
        return longest