class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []

        res = []

        firstPointer = secondPointer = 0
        while firstPointer < len(firstList) and secondPointer < len(secondList):
            firstValues = firstList[firstPointer]
            secondValues = secondList[secondPointer]
            interval = []
            
            if firstValues[0] > secondValues[1]:
                secondPointer+=1
                secondValues = secondList[secondPointer]

            if firstValues[0] < secondValues[0]:
                interval.append(secondValues[0])
            else:
                interval.append(firstValues[0])

            if firstValues[1] < secondValues[1]:
                interval.append(firstValues[1])
                firstPointer+=1
            else:
                interval.append(secondValues[1])
                secondPointer+=1

            if interval[0] > interval[1]:
                continue
            
            res.append(interval)

        return res