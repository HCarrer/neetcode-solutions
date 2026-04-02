class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if first smaller than last, is ordered
        if nums[0] <= nums[len(nums)-1]:
            return nums[0]
        
        numbers = set(nums)
        return min(numbers)