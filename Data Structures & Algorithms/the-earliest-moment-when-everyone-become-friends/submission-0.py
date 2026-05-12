class Union:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.groups = n
    
    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            minParent, maxParent = min(rootX, rootY), max(rootX, rootY)
            self.parent[maxParent] = minParent
            self.groups -= 1

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        friendGroups = Union(n)

        logs.sort(key=lambda x: x[0])

        for log in logs:
            timestamp, friend1, friend2 = log
            friendGroups.union(friend1, friend2)
            if friendGroups.groups == 1:
                return timestamp

        return -1