class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        
        maxSequence = 0
        for value in values:
            prev = value - 1
            if prev not in values:
                length = 0
                while value + length in values:
                    length += 1
                maxSequence = max(length, maxSequence)
            
        return maxSequence