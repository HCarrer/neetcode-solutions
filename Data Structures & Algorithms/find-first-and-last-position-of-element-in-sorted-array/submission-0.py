class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #[5,8,7,8,8,10]
        #[5,8,7],[8,8,10]
        #[5,8][7],[8,8][10]

        positionsHash = {}
        for index, num in enumerate(nums):
            if num not in positionsHash:
                positionsHash[num] = []
            positionsHash[num].append(index)

        if target not in positionsHash:
            return [-1,-1]

        return [min(positionsHash[target]),max(positionsHash[target])]