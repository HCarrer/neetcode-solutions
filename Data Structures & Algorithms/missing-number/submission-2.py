class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numsSet = set(nums)

        for num in range(max(nums)):
            print(numsSet, num)
            if not num in numsSet:
                return num
        return max(nums) + 1