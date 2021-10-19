from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        length = len(ratings)
        if length == 0:
            return 0
        pos, val = -1, float('inf')
        for i in range(length):
            if val > ratings[i]:
                val = ratings[i]
                pos = i

        r1 = self.helper(ratings[pos: ])
        # tmp = ratings[ :pos+1]
        r2 = self.helper(ratings[ :pos+1][ : :-1])
        return r1+r2-1

    def helper(self, ratings):
        length = len(ratings)
        if length == 0:
            return 0

        r = [0]*length

        r[0] = 1
        pre_val = ratings[0]
        pre_candy = r[0]
        for i in range(1, length):
            val = ratings[i]
            if val > pre_val:
                pre_candy += 1
            else:
                pre_candy = pre_candy-1 if pre_candy > 1 else 0
            r[i] = pre_candy
            pre_val = val
        return sum(r)

ratings = [1, 0 ,2]
ratings = [1,2,2]
ratings = [1,3,2,2,1]

so = Solution()
r = so.candy(ratings)
print(r)