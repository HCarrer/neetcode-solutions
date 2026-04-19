class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
            
        maxHeap = []
        for stone in stones:
            maxHeap.append(-1 * stone)
        heapq.heapify(maxHeap)

        while maxHeap:
            if len(maxHeap) == 1:
                return -1 * maxHeap[0]
            heaviest = -1 * heapq.heappop(maxHeap)
            secondHeaviest = -1 * heapq.heappop(maxHeap)
            print(maxHeap, heaviest, secondHeaviest)

            if heaviest == secondHeaviest:
                continue
            newStone = heaviest - secondHeaviest
            heapq.heappush(maxHeap, -1 * newStone)

        return 0