from typing import List

class Solution:
    def maxScore(self, nums):
        n,m = nums[0]
        scores = nums[1]

        r = []
        for i in range(2,m+2):
            ops, x, y  = nums[i]
            if ops == 'Q':
                r.append(max(scores[x-1:y]))
            else: # ops == 'U
                scores[x-1] = y
            
        return r

if __name__ == "__main__":
    nums = [
        [5 ,7],
[1 ,2, 3 ,4 ,5],
['Q' ,1, 5],
['U' ,3 ,6],
['Q' ,3 ,4],
['Q' ,4 ,5],
['U' ,4 ,5],
['U' ,2 ,9],
['Q' ,1 ,5] ,
    ]
    so = Solution()
    r = so.maxScore(nums)
    print(r)