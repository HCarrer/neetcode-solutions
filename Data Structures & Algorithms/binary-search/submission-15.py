class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            m = l + ((r-l) // 2)
            print(l, r, m, nums[m])
            if nums[m] <= target:
                l = m + 1
            else:
                r = m
        return l - 1 if (l and nums[l-1] == target) else -1