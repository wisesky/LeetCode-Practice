class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        le = len(nums)
        dp = []
        for i in range(le):
            dp.append(nums[i])

        for gap in range(1,le):
            for i in range(le-gap):
                j = i + gap
                dp[i] = max(nums[i] - dp[i+1], nums[j] - dp[i])
        #print(dp)
        return dp[0] >= 0

