class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 排列情况: #   对于满足 j>=nums[i-1]的所有j: dp[i] = sum(dp[i-1][j] +  dp[i][j-nums[i-1]]) )
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        for i in range(1, target+1):
            r = 0
            for num in nums:
                idx = i - num
                if idx >= 0:
                   r += dp[idx]
            dp[i] = r
        #print(dp)
        return dp[-1]

    # 组合情况 dp[i][j] = dp[i-1][j] + ( dp[i][j-nums[i-1]] if j >=nums[i-1] else 0 )
    def combinationSum4_1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 组合情况成立，而此题为排列情况
        dp = [ [0] * (target + 1) for _ in range(len(nums)+1)]
        # dp[1] = [1 for _ in range(target+1)]
        # dp[1][0] = 1
        for i in range(1, len(nums)+1):
            dp[i][0] = 1
            for j in range(1, target+1):
                dp[i][j] = dp[i-1][j] + ( (dp[i][j-nums[i-1]]) if j >= nums[i-1] else 0 )
                
        return dp

if __name__ == "__main__":
    nums = [1, 2, 3]
    target = 4
    so = Solution()
    print(so.combinationSum4(nums, target))
