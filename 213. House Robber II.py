class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
                return 0
        elif len(nums) <= 2:
                return max(nums)
        # def dp(nums):    
        #     dp = [0 for _ in range(len(nums))]
        #     dp[0] = nums[0]
        #     dp[1] = max(nums[0], nums[1])
        #     for i in range(2, len(nums)):
        #         dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        #     return dp[-1]
        return max(Solution.dp(nums[1: ]), Solution.dp(nums[ :-1]))

    @staticmethod
    def dp(nums):    
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[-1]