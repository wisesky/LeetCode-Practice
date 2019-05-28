class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.l = [0 for _ in nums]
        for i,num in enumerate(nums):
            self.l[i] = self.l[i-1] + num
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.l[j]
        return self.l[j] - self.l[i-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)