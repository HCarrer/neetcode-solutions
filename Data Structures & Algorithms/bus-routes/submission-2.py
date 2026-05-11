class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        adj = {}

        for bus in range(len(routes)):
            for stop in routes[bus]:
                if not stop in adj:
                    adj[stop] = []
                adj[stop].append(bus)

        q = deque([source])
        res = 0
        seenBuses = set()
        seenStops = set([source])
        while q:
            for _ in range(len(q)):
                currentStop = q.popleft()
                if currentStop == target:
                    return res
                for bus in adj.get(currentStop, []):
                    if bus in seenBuses:
                        continue
                    seenBuses.add(bus)
                    for nextStop in routes[bus]:
                        if nextStop in seenStops:
                            continue
                        seenStops.add(nextStop)
                        q.append(nextStop)
            res += 1

        return -1