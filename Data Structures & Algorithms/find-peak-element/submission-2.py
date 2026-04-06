class Solution:


    def findPeakElement(self, nums: List[int]) -> int:
        def binSearch(l: int, r: int) -> int:
            if l == r:
                return l
            m = l + (r-l) // 2
            if nums[m] < nums[m+1]:
                return binSearch(m+1, r)
            else:
                return binSearch(l, m)

        l, r = 0, len(nums) - 1
        return binSearch(l,r)