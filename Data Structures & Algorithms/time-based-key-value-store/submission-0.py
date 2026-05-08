class TimeMap:

    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.keys:
            self.keys[key] = []
        self.keys[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keys.get(key, [])        
        l, r = 0, len(values) - 1

        while l<=r:
            m = (r+l) // 2
            value, time = values[m]
            if time <= timestamp:
                res = value
                l = m + 1
            else:
                r = m - 1

        return res