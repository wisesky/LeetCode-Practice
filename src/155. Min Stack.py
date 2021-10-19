class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.minidx = []

    def push(self, x: int) -> None:
        self.nums.append(x)
        if len(self.minidx) == 0 or self.nums[self.minidx[-1]] > x:
            self.minidx.append(len(self.nums)-1)

    def pop(self) -> None:
        if self.minidx[-1] == len(self.nums) - 1:
            self.minidx.pop()
        self.nums.pop()

    def top(self) -> int:
        return self.nums[-1]

    def getMin(self) -> int:
        return self.nums[self.minidx[-1]]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()