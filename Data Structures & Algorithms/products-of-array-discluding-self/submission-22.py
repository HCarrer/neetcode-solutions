class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1] * len(nums)
        suf = [1] * len(nums)
        res = [1] * len(nums)

        # nums          [1,2,4,6]
        # pref          [1,1,2,8]

        # fill pref
        for i in range(1, len(nums)):
            pref[i] = pref[i-1] * nums[i-1]


        # nums         [1,2,4,6]
        # suf          [1,1,2,8]

        # fill suf
        for i in range(len(nums)-2, -1, -1):
            suf[i] = suf[i+1] * nums[i+1]

        for i in range(len(nums)):
            res[i] = pref[i] * suf[i]

        return res