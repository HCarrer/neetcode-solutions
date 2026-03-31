class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        l,r = 0,len(heights)-1
        while l<r:
            leftWall, rightWall = heights[l], heights[r]
            maxHeight = min(leftWall, rightWall)
            area = maxHeight * (r-l)
            largest = max(largest, area)
            if leftWall <= rightWall:
                l+=1
            else:
                r-=1
        return largest