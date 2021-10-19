#
# @lc app=leetcode id=330 lang=python3
#
# [330] Patching Array
#
# https://leetcode.com/problems/patching-array/description/
#
# algorithms
# Hard (35.33%)
# Likes:    891
# Dislikes: 102
# Total Accepted:    49.9K
# Total Submissions: 130.1K
# Testcase Example:  '[1,3]\n6'
#
# Given a sorted integer array nums and an integer n, add/patch elements to the
# array such that any number in the range [1, n] inclusive can be formed by the
# sum of some elements in the array.
# 
# Return the minimum number of patches required.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,3], n = 6
# Output: 1
# Explanation:
# Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3,
# 4.
# Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3],
# [2,3], [1,2,3].
# Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
# So we only need 1 patch.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,5,10], n = 20
# Output: 2
# Explanation: The two patches can be [2, 4].
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,2], n = 5
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 10^4
# nums is sorted in ascending order.
# 1 <= n <= 2^31 - 1
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        """
        memory error
        思路是，[1,n]遍历，遇到没办法Cover 的数，直接添加进nums，
        然后更新可达目标
        因为有可能会出现，构成tgt 的元素有重复，如果需要验证和排除这个重复情况
        用dp来记录构成val，需要的nums集合构成，用二进制表示集合

        步骤：
        1 
        """
        length = len(nums)
        if nums[0] != 1 :
            nums = [1] + nums
        # dp = [0] * (n+1)
        dp = {}
        dp[1] = True
        for val in range(1,n+1):
            pos = self.biLeftSearch(nums, val)
            if pos < len(nums) and nums[pos] == val:
                dp[val] = 1 << val
                continue
            if not self.isCover(nums[ :pos], val, dp):
                nums = nums[ :pos] + [val] + nums[pos: ]
                
        return nums

    def biLeftSearch(self, nums, val):
        """
        binary search left boundry
        """
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi-lo)//2
            if val <= nums[mid]:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def isCover(self, nums, val, dp):
        # if val in dp:
        #     return True
        for i in range(len(nums)):
            num = nums[i]
            rest = val - num
            if dp.get(rest, 0)!=0 and dp[rest] & (1<<i) == 0:
                dp[val] = dp[rest] | (1<<i)
                return True
            # if self.isCover(nums[ :i], rest, dp):
            #     dp[val] = True
            #     return True
        else:
            return False

    def minPatches(self, nums, n):
        """
        dfs search
        """
        # (m, val) -> 是否存在 在nums[ :m] 中可以得到val的
        memo = {} 
        for val in range(1, n+1):
            flag, pos = self.dfs(nums, val)
            if not flag:
                nums = nums[ :pos] + [val] + nums[pos: ]
        return nums
    
    def dfs(self, nums, val):
        """
        search in nums for val
        """
        pos = self.biLeftSearch(nums, val)
        if pos<len(nums) and nums[pos] == val:
            return True, None
        
        for j in range(pos-1, -1,-1):
            rest = val - nums[j]
            flag, _ = self.dfs(nums[ :j], rest)
            if flag:
                return True, None
        else:
            return False, pos

    def minPatches(self, nums, n):
        """
        151ms(5%) 14.4MB(65%)
        跟 coins change 类似，可以遍历统计由 有限的 nums 构建目标数值tgt的时候
        是否能存在这样的组合，限制是每个数只能选择一次 可以归属为 0-1背包问题
        dp[m][tgt]: 在 nums[ :m] 中 tgt 是否可达
        dp[0][*] : False 不可达
        dp[*][0]: True 可达
        dp[m][tgt] = dp[m-1][tgt] or dp[m-1][tgt-val_m]: when tgt>=val_m

        在草稿上演绎过一遍算法流程，很快就会发现，只需要一行数组即可
        因为 dp[m][*] 只依赖于 dp[m-1][*]
        除此之外，发现 dp数组的特点是， 
        a>, 一定存在在某个位置 pos , dp[m][ :pos]全是1， dp[m][pos: ]全是0
        且 dp[m][*] 相对于 dp[m-1][*] 只是把 pos的位置扩大了而已，
        扩大方式是把dp[m-1][ :pos]中的1 全部往后平移 val 个位置 然后与dp[m][*] 求｜合并，这个val就是 nums[m]
        如果合并之后不满足 上述特点a>, 那么就会出现空缺，不满足条件，那么此时就需要添加新num -> nums
        
        至此，就完全极简化了算法流程
        """
        
        # [left, right)
        left, right = 0,1 # row_1 
        count = 0
        # for i in range(1,len(nums)):
        #     new_left, new_right = left+nums[i], right+nums[i]
        #     if right < new_left:
        #         nums = nums[ :i] + [right] + nums[i: ]
        #         left = 0
        #         right = 2*right
        #         count += 1
        #     else:
        #         left = 0
        #         right = new_right
            
        i = 0
        while i < len(nums):
            new_left = left + nums[i]
            new_right = right + nums[i]
            if right < new_left:
                # nums = nums[ :i] + [right] + nums[i: ]
                left = 0
                right = 2*right
                count += 1
            else:
                left = 0
                right = new_right
                i += 1
            if right > n :
                break

        while right <= n:
            right = 2*right
            count += 1

        return count

# @lc code=end

so = Solution()

nums = [1,5,10]
n = 20

nums = [1,3]
n = 6

nums = [1,2,2]
n = 5

nums = [1,2,31,33]
n = 2147483647

nums = [1,2,3]
n = 2147483647

nums = [10,30,36,42,50,76,87,88,91,92]
n = 54

nums = [1,7,21,31,34,37,40,43,49,87,90,92,93,98,99]
n = 12
print(so.minPatches(nums, n))