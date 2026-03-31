class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1] * n
        suf = [1] * n
        
        # pref
        for i in range(n):
            if i == 0:
                continue
            pref[i] = pref[i-1] * nums[i-1]
        
        # suf
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                continue
            suf[i] = suf[i+1] * nums[i+1]
            
        res = [0] * n
        for i in range(0, n):
            res[i] = pref[i] * suf[i]
                
        return res