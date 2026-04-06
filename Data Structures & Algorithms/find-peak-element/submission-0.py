class Solution:
    def binSearch(self, l: int, r: int, nums: List[int]) -> int:
        if l == r:
            return l
        m = l + (r-l) // 2
        if nums[m] < nums[m+1]:
            return self.binSearch(m+1, r, nums)
        else:
            return self.binSearch(l, m, nums)


    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        return self.binSearch(l,r,nums)