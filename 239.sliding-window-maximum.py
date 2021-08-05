#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
# https://leetcode.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (45.18%)
# Likes:    6492
# Dislikes: 245
# Total Accepted:    422.6K
# Total Submissions: 934.4K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# You are given an array of integers nums, there is a sliding window of size k
# which is moving from the very left of the array to the very right. You can
# only see the k numbers in the window. Each time the sliding window moves
# right by one position.
# 
# Return the max sliding window.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
# 
# 
# Example 2:
# 
# 
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,-1], k = 1
# Output: [1,-1]
# 
# 
# Example 4:
# 
# 
# Input: nums = [9,11], k = 2
# Output: [11]
# 
# 
# Example 5:
# 
# 
# Input: nums = [4,-2], k = 2
# Output: [4]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length
# 
# 
#
from typing import List
from collections import deque
# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        借鉴 shell sort ，从winsize=1 逐步扩张到 winsize=k ，每次只需要比较 新入windows的num 和原winsize_max 之间的大小即可
        O(kn)
        But LTE
        """
        res = nums.copy()
        length = len(nums)
        for i in range(2,k+1):
            for j in range(length-i+1):
                res[j] = max(res[j], nums[j+i-1])
        return res[ :length-k+1]

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]: 
        """
        滑动窗口法， 每次滑动 - first + last ，然后判断 max(windows)
        O(nk)
        but LTE
        """       
        res = []
        maxVal, maxPos = float('-inf'), None
        for i, num in enumerate(nums[ :k]):
            if num >= maxVal:
                # preVal, prePos = maxVal, maxPos
                maxVal, maxPos = num, i

        res.append(maxVal)
        length = len(nums)
        for i in range(k,length):
            curVal = nums[i]
            if curVal >= maxVal:
                # preVal, prePos = maxVal, maxPos
                maxVal, maxPos = curVal, i
                # res.append(maxVal)
            elif maxPos > i-k:
                # res.append(maxVal)
                pass
            else:
                # maxVal, maxPos = preVal, prePos
                maxVal = max(nums[i-k+1:i+1])
                maxPos = [pos for pos in range(i-k+1, i+1) if nums[pos]==maxVal][-1]
                
            res.append(maxVal)
        return res

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        初始设想是维护一个 堆 或者 优先队列，同时还能随时 remove 其中任意一个节点，
        因为要维护一个 windows 内的元素，必须要能删除 windows first 元素的接口，
        尽管 java PriorityQueue 中有 remove 接口，但是python的 heapq ,priority queue 都没有类似的接口
        否则就可以用如下算法实现：
            for i in range(len(nums)):
                if len(maxque) >= k:
                    maxque.remove(nums[i-k])
                maxque.put(nums[i])
                if i>=k-1:
                    result.append(maxque.peek())

        退而求其次： 插入排序法 insert sort
        维护一个递减序列， 采取插入排序法插入新增的元素，同时根据索引的范围，来定向删除 滑动widnows之后的first 元素
        time: O(nk)
        but LTE
        """           
        length = len(nums)
        # insert sort
        insert = []
        for i in range(k):
            insert.append(i)
            for j in range(len(insert)-1, 0,-1):
                pre = nums[insert[j-1]]
                cur = nums[insert[j]]
                if pre > cur:
                    tmp = insert[j]
                    insert[j] = insert[j-1]
                    insert[j-1] = tmp
                else:
                    break

        res = [ nums[insert[-1]] ]
        for i in range(k, length):
            insert.remove(i-k)
            insert.append(i)
            for j in range(len(insert), 0,-1):
                pre = nums[insert[j-1]]
                cur = nums[insert[j]]
                if pre > cur:
                    tmp = insert[j]
                    insert[j] = insert[j-1]
                    insert[j-1] = tmp
                else:
                    break
            res.append(nums[insert[-1]])
        return res
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:            
        """
        deque insert
        基于观察可知： 位置靠后， val值更大，是更加有竞争力的 candidates
        维护一个滑动窗口[i-k+1, i]内的 promising 递减序列 maxQue： 保持原列表次序+递减
        1, 维护滑动窗口[i-k+1, i]，由于maxQue维持了队伍 次序，队首就是需要删除的最先入列的需要删除的值
            且有可能队伍 的原队首 在 步骤2中已经被淘汰掉了，所以需要判断一下是否真的是需要删除的first
        2, 维护一个递减的maxQue，且不打乱原列表次序，如果次序x 比 i 更靠前 的 nums[x] 比 nums[i] 小，直接淘汰掉，
            因为有nums[i] 在的窗口中，一定不存在这样更靠前的值更小的val_x：x 被选中的可能
        3, 这样就得到了 维持原队列次序 的 递减序列
        """
        length = len(nums)
        maxQue = deque()
        r = []
        for i in range(length):
            # if i >= k  and maxQue[0] == nums[i-k]:
            # if i >= k  and maxQue[0] == i-k:
                # maxQue.popleft()
            # 2. 循环删除 队首的 超出窗口[i-k+1, i] 的索引值
            # while len(maxQue)!=0 and maxQue[0] < i-k+1:
            # 2.1 优化 由于maxQue 保持了原队列次序，那么 队首的值一定是次序最靠前的那一个
            # if len(maxQue)!=0 and maxQue[0] < i-k+1:
            # 2.2 优化 由于只有可能队首是需要删除的，那么直接判断即可
            if len(maxQue)!=0 and maxQue[0] == i-k:
                maxQue.popleft()
            while len(maxQue)!=0 and nums[maxQue[-1]] < nums[i]:
                maxQue.pop()
            
            # maxQue.append(nums[i])
            maxQue.append(i)
            if i >= k-1:
                r.append(nums[maxQue[0]])
        return r
            
    # @lc code=end

if __name__ == '__main__':
    so = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    # nums =   [7,2,4]
    # k = 2
    res = so.maxSlidingWindow(nums, k)
    print(res)
