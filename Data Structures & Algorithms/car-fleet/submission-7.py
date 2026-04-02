class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        orderedCars = [(p, s) for p, s in zip(position, speed)]
        orderedCars.sort(reverse=True)

        fleets = 1
        prevTime = (target - orderedCars[0][0]) / orderedCars[0][1]
        for i in range(len(orderedCars)):
            carTime = (target - orderedCars[i][0]) / orderedCars[i][1]
            if carTime > prevTime:
                fleets += 1
                prevTime = carTime
        return fleets
