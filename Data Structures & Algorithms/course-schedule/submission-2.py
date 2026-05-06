class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReqMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preReqMap[crs].append(pre)

        visited = set()

        def dfs(course):
            # detectou loop
            if course in visited:
                return False

            # if preReqMap[course] == []:
            #     return True

            visited.add(course)
            for preReq in preReqMap[course]:
                if not dfs(preReq):
                    return False
            visited.remove(course)

            preReqMap[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True