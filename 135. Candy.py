from typing import List

class Solution:
    # s1 
    # 归纳起来数组模式是 bottom -> peak -> bottom -> equal 的组合，可能存在中间的peak ,bottom 或者 equal 不存在的特例
    # 计算左半边和右半边的长度，直接就可以根据等差数列得出sum
    # 唯一需要确定的是peak的candy值，这个值可以根据左半边和右边长度的最大值推断出
    def candy(self, ratings: List[int]) -> int:
        length = len(ratings)
        if length == 0:
            return 0

        start = 0
        sum_candy = 1 # init previous round bottom sum =1, because -1 each round to correct bottom double count problem
        i = 0
        while i < length-1: # cur = i, next = i+1
            # botton -> peak : peak not included
            while i<length-1 and ratings[i] < ratings[i+1]:
                i += 1
            left = i - start
            start = i
            # peak -> next bottom : peak not included
            while i<length-1 and ratings[i] > ratings[i+1]:
                i += 1
            right = i - start
            start = i
            # count peak_candy and sum_candy
            peak_candy = max(left, right) + 1
            sum_candy += (left+1)*left//2 + (right+1)*right//2 + peak_candy - 1 # - 1 because left bottom included by previous round
            # handle equal 
            while i<length-1 and ratings[i] == ratings[i+1]:
                i += 1
                sum_candy += 1
            start = i

        return sum_candy


ratings = [1,0,2]
ratings = [1,2,2]
ratings = [1,3,2,1]
# ratings = [1,3,2,2,1]
# ratings = [1,2,87,88,87,4,3,2,1]
# ratings = [1,3,4,5,2]
# ratings = [0,1,2,5,3,2,7]

so = Solution()

res = so.candy(ratings)
print(res)