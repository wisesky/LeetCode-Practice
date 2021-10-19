from typing import List
from copy import deepcopy

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        matrix = [['.']*n for _ in range(n)]
        unchosen = []
        for x in range(n):
            # row = []
            for y in range(n):
                # row.append((x,y))
                unchosen.append((x,y))

        unchosen = set(unchosen)
        res = []
        self.helper(matrix, n, unchosen, n, res)
        result = [x.split(',') for x in res]
        return result

    def helper(self, matrix, left, unchosen,n, res):
        if left == 0:
            r = [''.join(x) for x in matrix]
            str_r = ','.join(r)
            if str_r not in res:
                res.append(str_r)
            return

        if len(unchosen) == 0:
            return
        
        # for choice in unchosen:
            # x, y = choice
        x = n - left
        # unchosen = unchosen - set([(x, i) for i in range(n)])
        for y in range(n):
            if (x,y) not in unchosen:
                continue
            conArea = self.conflictArea(x, y,n)
            matrix[x][y] = 'Q'
            self.helper(matrix, left-1, unchosen - conArea, n, res)
            matrix[x][y] = '.'
        return

    def conflictArea(self,x,y, n):
        rowArea = [(x, j) for j in range(n)]
        colArea = [(i, y)for i in range(n)]
        otherArea = []

        st,ed = x, y
        while st in range(n) and ed in range(n):
            otherArea.append((st,ed))
            st += 1
            ed += 1

        st,ed = x, y
        while st in range(n) and ed in range(n):
            otherArea.append((st,ed))
            st -= 1
            ed -= 1

        st,ed = x, y
        while st in range(n) and ed in range(n):
            otherArea.append((st,ed))
            st += 1
            ed -= 1

        st,ed = x, y
        while st in range(n) and ed in range(n):
            otherArea.append((st,ed))
            st -= 1
            ed += 1

        return set(rowArea + colArea + otherArea)

if __name__ == "__main__":
    
    so = Solution()
    res = so.solveNQueens(4)
    for r in res:
        print(r)
        print('-'*30)