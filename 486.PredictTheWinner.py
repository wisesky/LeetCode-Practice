class Solution:
    # s1 dp
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        le = len(nums)
        dp = [] # dp[i] 表示 nums[i:i+gap] 的list 作为 player1 净胜多少分数
        # gap = 0 即单个元素组成的数组 给player1 先选， 净胜分数就是单数组元素大小
        for i in range(le):
            dp.append(nums[i])

        for gap in range(1,le):
            for i in range(le-gap):
                j = i + gap
                dp[i] = max(nums[i] - dp[i+1], nums[j] - dp[i])
        #print(dp)
        return dp[0] >= 0

    # s2 dfs
    def PredictTheWinner(self, nums):
        

    def helper(self, nums, res, player1=True):
        if len(nums) == 1:
            return res + nums >= 0 if player1 else res+nums > 0
        head = res[0]
        tail = res[-1]
        player = not player1
        return self.helper(nums[1: ], -res, player1=player) or self.helper(nums[ :-1], -res, player1=player):
    

nums = [1,5,2]
nums = [1, 5, 233, 7]
so = Solution()
print(so.PredictTheWinner(nums))