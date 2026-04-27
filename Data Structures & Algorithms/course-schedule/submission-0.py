class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReqMap = {i: [] for i in range(numCourses)}
        for course, preReq in prerequisites:
            preReqMap[course].append(preReq)

        computed = set()

        def dfs(course):
            if course in computed:
                return False

            # se nao tiver prerequisitos
            if preReqMap[course] == []:
                return True

            computed.add(course)
            for preReq in preReqMap[course]:
                if not dfs(preReq):
                    return False
            computed.remove(course)
            preReqMap[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True