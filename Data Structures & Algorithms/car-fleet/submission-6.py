class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # carsArrived = 0
        # fleets = 0
        # arrivalStack = []
        # # loop until all cars have arrived
        # arrivals = 0
        # while carsArrived <= len(position):
        #     for index, pos in enumerate(position):
        #         if pos == target:
        #             carsArrived+=1
        #             arrivalStack.append(index)
        #         position[index] = pos + speed[index]
        #     print(position)
        #     break
        # return carsArrived

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
