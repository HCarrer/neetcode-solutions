class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashTable = {}
        for i, n in enumerate(nums):
            if n in hashTable:
                return True
            hashTable[n] = i
        return False