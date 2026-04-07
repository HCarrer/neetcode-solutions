class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # target = 1
        # [3,4,5,6,1,2]
        # [6,1,2]
        def binarySearch(target):
            l = 0
            r = len(nums)-1
            while l<=r:
                m = (l+r) // 2
                if target == nums[m]:
                    return m

                if nums[l] <= nums[m]: # left half
                    if target < nums[l] or target > nums[m]:
                        l = m+1
                    else:
                        r = m-1
                else: # right half
                    if target < nums[m] or target > nums[r]:
                        r = m-1
                    else:
                        l = m+1
            return -1
        
        return binarySearch(target)