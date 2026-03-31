class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and n == nums[i - 1]:
                continue
            j,k = i+1,len(nums)-1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum < 0:
                    j+=1
                if sum > 0:
                    k-=1
                if sum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                
        return res