class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1Idx = {num: i for i, num in enumerate(nums1)}
        res = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            n = nums2[i]

            while stack and n > stack[-1]:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = n
            if n in nums1Idx:
                stack.append(n)

        return res