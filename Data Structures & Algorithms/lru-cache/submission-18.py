class LRUCache:

    def __init__(self, capacity: int):
        self.map = OrderedDict()
        self.capacity = capacity
        self.filled = 0
        self.usedStack = []

    def get(self, key: int) -> int:
        print("getting", key)
        if key not in self.map:
            return -1
        self.map.move_to_end(key)
        return self.map[key]

    def put(self, key: int, value: int) -> None:
        print("adding", key,"->", value)
        exists = key in self.map
        self.map[key] = value
        if exists:
            self.map.move_to_end(key)
        else:
            if len(self.map) > self.capacity:
                self.map.popitem(last=False)
