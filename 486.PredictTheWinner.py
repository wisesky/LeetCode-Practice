class Solution:
    # s1 dp
    # def PredictTheWinner(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: bool
    #     """
    #     le = len(nums)
    #     dp = [] # dp[i] 表示 nums[i:i+gap] 的list 作为 player1 净胜多少分数
    #     # gap = 0 即单个元素组成的数组 给player1 先选， 净胜分数就是单数组元素大小
    #     for i in range(le):
    #         dp.append(nums[i])

    #     for gap in range(1,le):
    #         for i in range(le-gap):
    #             j = i + gap
    #             dp[i] = max(nums[i] - dp[i+1], nums[j] - dp[i])
    #     #print(dp)
    #     return dp[0] >= 0

    # s2 dfs
    def PredictTheWinner(self, nums):
        result = self.helper(nums)
        return result >= 0

    def helper(self, nums):
        if len(nums) == 1:
            return nums[0] 
        head = nums[0]
        tail = nums[-1]
        r = max(head-self.helper(nums[1: ]) , tail-self.helper(nums[ :-1]) )
        return r
    

nums = [1,5,3]
# nums = [1, 5, 233, 7]
so = Solution()
print(so.PredictTheWinner(nums))