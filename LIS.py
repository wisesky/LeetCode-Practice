class Solution:
    def longestIncreasingSequence(self, nums):
        l = len(nums)
        dp = [1 for _ in range(l+1)]
        seqTo = {}
        #dp[0] = 1
        for i, num in enumerate(nums):
            v = dp[i]
            for j in range(i):
                if nums[j] < num:
                    if v < dp[j] + 1:
                        seqTo[i] = j
                        v = dp[j] + 1
                    # v = max(v, dp[j] + 1)
                    
            dp[i] = v
        print(dp)
        print(seqTo)
        idx = dp.index(max(dp))
        res = []
        while idx != None:
            res.insert(0, nums[idx])
            idx = seqTo.get(idx)
        print(res)
        return 0
if __name__ == "__main__":
    dp = [4,5,6,3]
    #dp = [4,5,6,3,8]
    so = Solution()
    res = so.longestIncreasingSequence(dp)
    #print(res)
