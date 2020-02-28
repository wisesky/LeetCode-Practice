import bisect
class Solution:
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        lr = len(matrix)
        lc = len(matrix[0])
        res = float('-inf')

        for left in range(lc):
            sums = [0 for _ in range(lr)]
            for right in range(left, lc):
                for i in range(lr):
                    sums[i] += matrix[i][right]
                curSet = [0]
                curCum = 0
                curMax = float('-inf')
                for sum in sums:
                    curCum += sum
                    it = bisect.bisect_left(curSet, curCum - k)
                    if  0 <= it < len(curSet):
                        curMax = max(curMax, curCum - curSet[it])
                    #curSet.append(curCum)
                    # using insort instead of append since bisect_left reason
                    bisect.insort(curSet, curCum)
                res = max(res, curMax)

        return res
    
