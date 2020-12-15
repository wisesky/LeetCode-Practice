from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        r = [1]
        for i in range(1, rowIndex+1):
            r_next = [0]*(i+1)
            r_next[0], r_next[-1] = 1,1

            space = len(r_next) - 2

            if space > 0 :
                for j in range(space):
                    r_next[j+1] = r[j] + r[j+1]
            
            r = r_next

        return r

so = Solution()
print(so.getRow(0))