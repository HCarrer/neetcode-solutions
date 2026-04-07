class Solution:


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(target):
            l,r=0, len(nums)
            while l < r:
                m = l+(r-l) // 2
                if nums[m] >= target:
                    r = m
                else:
                    l = m+1
            return l

        start = binarySearch(target)
        if start == len(nums) or nums[start] != target:
            return [-1,-1]

        return [start, binarySearch(target + 1) - 1]