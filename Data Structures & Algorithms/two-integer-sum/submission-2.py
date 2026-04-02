class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in values:
                return [index, values[diff]] if index < values[diff] else [values[diff], index]
            values[num] = index
        
