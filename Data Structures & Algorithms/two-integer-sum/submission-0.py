class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashTable:
                returnArr = [hashTable[diff], i]
            hashTable[n] = i
        
        return [returnArr[0], returnArr[1]] if returnArr[0] < returnArr[1] else [returnArr[1], returnArr[0]]