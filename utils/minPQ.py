class MinPQ:
    def __init__(self, vals=[]) -> None:
        self.vals = [-1] + vals
        self.n = len(vals)

    def insert(self, val):
        self.vals.append(val)
        self.n += 1
        self.swim(self.n)

    def min(self):
        return self.vals[1]

    def delMin(self):
        if self.isEmpty():
            return None
        minVal = self.vals[1]
        self.exch(1, -1)
        self.n -= 1
        self.sink(1)
        self.vals.pop()
        assert len(self.vals) == self.n+1
        return minVal

    def isEmpty(self):
        return self.n == 0

    def size(self):
        return self.n

    def swim(self, x):
        while x > 1 and self.greater(x//2, x):
            self.exch(x//2, x)
            x = x // 2

    def sink(self, x):
        while 2*x <= self.n:
            son = 2 * x
            if son < self.n and self.greater(son,son+1):
                son += 1
            if not self.greater(x, son):
                break
            self.exch(son, x)
            x = son

    def exch(self, i, j):
        swp = self.vals[i]
        self.vals[i] = self.vals[j]
        self.vals[j] = swp

    def greater(self, i, j):
        return self.vals[i] > self.vals[j]

import random
# vals = [5, 10, 19, 18, 20, 24, 29, 24, 19, 27]
vals = []
pq = MinPQ(vals)
for i in range(10):
    pq.insert(random.randrange(30))

print(pq.vals)
print('-'*50)
while not pq.isEmpty():
    print(pq.delMin())