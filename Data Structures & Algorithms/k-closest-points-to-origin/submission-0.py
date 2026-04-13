class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for index, point in enumerate(points):
            x,y = point[0], point[1]
            distanceToOrigin = math.sqrt((x ** 2) + (y ** 2))
            points[index] = (distanceToOrigin, [x,y])

        heapq.heapify(points)
        res = []
        while k > 0:
            distance, coords = heapq.heappop(points)
            res.append(coords)
            k-=1

        return res