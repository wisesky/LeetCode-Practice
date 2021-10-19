from typing import List
from itertools import product
import random

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # s1 inmitate std practice
        # nums = list(range(1,n+1))
        # res = self.combinations(nums, k)
        # return list(res)

        # s2 DFS
        # nums = list(range(1, n+1))
        # marked = ['0']*n
        # res = []
        # flag = False
        # if k > n//2:
        #     k = n-k
        #     flag = True
        # self.myCombinations(nums, k, marked, res)
        # result = []
        # for r in res:
        #     tmp = []
        #     for i, mark in enumerate(r):
        #         if not flag:
        #             if mark == '1':
        #                 tmp.append(nums[i])
        #         else:
        #             if mark == '0':
        #                 tmp.append(nums[i])
        #     result.append(tmp)
        # return result

        # s3 optim DFS
        nums = list(range(1,n+1))
        res = []
        self.myCombinations_1(nums, k, 0, [],res)
        return res

    def combinations(self, nums, k):
        n = len(nums)
        for indices in product(range(n), repeat=k):
            if len(set(indices)) == len(indices) and sorted(indices) == list(indices):
                yield [nums[i] for i in indices]

    # DFS
    def myCombinations(self, nums, k, marked, res):
        if k == 0:
            str_marked = ''.join(marked)
            if str_marked not in res:
                res.append(str_marked)
            return
        
        for i, num in enumerate(nums):
            if  marked[i] == '0':
                marked[i] = '1'
                self.myCombinations(nums, k-1, marked, res)
                marked[i] = '0'
        return

    # optim DFS
    def myCombinations_1(self, nums, k, start, r,res):
        if len(r) == k :
            r_copy = r.copy()
            res.append(r_copy)
            return
        
        for i in range(start, len(nums) - (k-len(r)) + 1):
            r.append(nums[i])
            self.myCombinations_1(nums, k, i+1, r, res)
            r.pop()
        return

if __name__ == "__main__":
    so = Solution()
    n = 9
    k = 8
    res = so.combine(n, k)
    for r in res:
        print(r)