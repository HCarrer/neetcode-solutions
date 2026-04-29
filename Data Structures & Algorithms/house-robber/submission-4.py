class Solution:
    def rob(self, nums: List[int]) -> int:
        memoArr = [-1] * len(nums)

        def dfs(index):
            if index >= len(nums):
                return 0
            
            if memoArr[index] != -1:
                return memoArr[index]

            memoArr[index] = max(dfs(index+1), nums[index] + dfs(index+2))

            return memoArr[index]

        return dfs(0)
