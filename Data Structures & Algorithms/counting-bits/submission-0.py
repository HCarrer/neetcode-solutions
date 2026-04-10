class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        for i in range(n+1):
            for j in range(32):
                mask = (1 << j)
                if mask & i:
                    res[i] += 1
        return res