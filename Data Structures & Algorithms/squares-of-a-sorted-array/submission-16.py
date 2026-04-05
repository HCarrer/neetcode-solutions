class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        insertionIndex = len(nums) - 1

        l, r = 0, len(nums) - 1

        while insertionIndex >= 0:
            absL, absR = abs(nums[l]), abs(nums[r])
            if absL < absR:
                res[insertionIndex] = absR**2
                r-=1
            else:
                res[insertionIndex] = absL**2
                l+=1
            insertionIndex -= 1
        return res