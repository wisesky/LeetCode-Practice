from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(1, numRows+1):
            r = [0]*i
            r[0],r[-1] = 1,1
            space = i - 2

            if space > 0:
                for j in range(space):
                    r[j+1] = res[-1][j] + res[-1][j+1]
            res.append(r)
        return res

so = Solution()
res = so.generate(6)
print(res)