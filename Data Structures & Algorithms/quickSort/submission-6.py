# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def helper(self, arr: List[Pair], start: int, end: int) -> None:
        if end - start + 1 <= 1:
            return

        pivot = arr[end]
        left = start
        for i in range(start,end):
            if arr[i].key < pivot.key:
                arr[i], arr[left] = arr[left], arr[i]
                left += 1
            
        arr[end] = arr[left]
        arr[left] = pivot
        
        self.helper(arr, start, left-1)
        self.helper(arr, left+1, end)

    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.helper(pairs, 0, len(pairs)-1)
        return pairs
    