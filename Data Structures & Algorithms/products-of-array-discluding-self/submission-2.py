class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for i, numI in enumerate(nums):
            mult = 1
            for j, numJ in enumerate(nums):
                if i == j:
                    continue
                mult = mult * numJ
            res.append(mult)
        return res