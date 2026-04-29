class Solution:
    def climbStairs(self, n: int) -> int:
        ways = 0

        visited = [-1] * n

        def dfs(currentSteps):
            if currentSteps >= n:
                return currentSteps == n

            if visited[currentSteps] != -1:
                return visited[currentSteps]

            visited[currentSteps] = dfs(currentSteps + 1) + dfs(currentSteps + 2)

            return visited[currentSteps]

        return dfs(0)

        