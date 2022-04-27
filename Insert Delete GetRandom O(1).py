import random


class RandomizedSet:
    def __init__(self):
        self.map = dict()
        self.idx = 0
        self.list = []

    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.map[val] = self.idx
            self.list.append(val)
            self.idx += 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.map:
            del_idx = self.map[val]
            last = self.list[-1]
            self.list[del_idx] = last
            self.map[last] = del_idx
            self.map.pop(val)
            self.list.pop()
            self.idx -= 1
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.list)
