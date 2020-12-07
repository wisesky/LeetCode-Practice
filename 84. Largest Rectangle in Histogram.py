from typing import List

class Solution:
    # s1 暴力解法
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0
        # dp = [[num, num] for num in heights]
        dp = heights.copy()
        dp_max = max(dp)
        for gap in range(1, len(heights)):
            for i in range(len(heights)-gap):
                # j = i+gap
                dp[i] = min(dp[i], dp[i+1])
            tmp_max = max(dp[ :-gap])
            dp_max = max(dp_max, tmp_max * (gap+1))

        return dp_max

    # s2 求 一定包含当前柱的矩形面积
    # 一定包含当前的边界条件是， 刚好比当前柱高度 h 小。
    # 所以需要求刚好比h小的左边界，leftidx
    # 刚好比h小的右边界，rightidx
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0
        length = len(heights)
        leftidx = [-1]*length
        rightidx = [length]*length

        for i in range(1,length):
            pos = i - 1
            val_i = heights[i]
            while pos >= 0 and heights[pos] >= val_i:
                # pos -= 1
                # O(n**2) --> O(n) Tricks
                # 如果 左边pos的柱高度heights[pos]比当前val大， 
                # 那么左边pos的左边界leftidx[pos]肯定比当前i的左边界更大,以此作为新起点往左边遍历
                # 注意左边边界的终点设置为 -1 
                pos = leftidx[pos]

            leftidx[i] = pos

        for j in range(length-2, -1, -1):
            pos = j+1
            val_j = heights[j]
            while pos < length and  heights[pos] >= val_j:
                # pos += 1
                # O(n**2) --> O(n) Tricks
                # 原理同上，只不过右边界的终点是 length
                pos = rightidx[pos]
            
            rightidx[j] = pos

        res_max = float('-inf')
        for i in range(length):
            itv = rightidx[i] - leftidx[i] - 1
            res_max = max(res_max, itv * heights[i])

        return res_max

    # s3 利用堆栈优化实现s2
    # stack 用来保存递增序列的索引，
    # 碰到当前元素比栈顶元素小的时候， 就可以开始计算以栈顶cur为中心的矩形大小， 
    # 当前元素恰好比栈顶小，就是此矩形的右边界
    # 堆栈里栈顶之后下面的元素比栈顶小，就是此矩形的左边界
    # 最后注意，当heights 遍历完之后，堆栈可能还有元素，此时的情况是堆栈里所有元素的右边界就是 length
    # 以此为依据可以开始清空堆栈
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        if length == 0:
            return 0
        stack = []
        res = 0
        for i in range(length):
            val_i = heights[i]
            post_idx = i
            while len(stack) > 0 and val_i < heights[stack[-1]]:
                cur_idx = stack.pop()
                cur_val = heights[cur_idx]
                pre_idx = stack[-1] if len(stack) > 0 else -1
                itv = post_idx - pre_idx - 1
                res = max(res, itv * cur_val)

            stack.append(i)

        post_idx = length
        while len(stack) > 0:
            cur_idx = stack.pop()
            cur_val = heights[cur_idx]
            pre_idx = stack[-1] if len(stack) > 0 else -1
            itv = post_idx - pre_idx - 1
            res = max(res, itv * cur_val)
            
        return res

    # s4 优化堆栈法s3 可以通过给heights 人工添加右边界柱高值0，
    # 并给堆栈stack赋予左边界索引初值-1,同时柱高值就是就是heights[-1] ，也就是0，正好也是边界应该有的柱高值
    # 可以简化很多判断，诸如 len(stack) > 0 , 最后的清空堆栈过程，在添加右边界元素0的清空下，可以省略
    # 最后stack 剩下的就是 柱高为0的索引，作为边界，无需处理
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        length = len(heights)
        res = 0
        # 由于 heigth.append(0) 所以有了初值
        # if length == 1:
        #     return 0
        for i in range(length):
            while heights[stack[-1]] > heights[i]  :
                h = heights[stack.pop()]
                # as  post_idx = i, pre_idx = stack[-1]
                # so itv = post_idx - pre_idx -1
                itv = i - stack[-1] - 1
                res = max(res, itv * h)
            stack.append(i)
        heights.pop()
        return res

heights = [5,9,10]
heights = [2,1,5,6,2,3]
# heights = list(range(10000))
so = Solution()
r = so.largestRectangleArea(heights)
print(r)