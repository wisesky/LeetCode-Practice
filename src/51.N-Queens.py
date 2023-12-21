from typing import List
from copy import deepcopy

class Solution:
    # 朴素DFS算法，利用helper函数来搜索可以摆放的空间，
    # 1，一旦搜索到，存到res中，
    # 2， 如果搜索空间耗尽，则返回
    # 3， conflictArea 依据摆放位置(x,y)，遍历所有不合法空间，存起来到conArea,unchosen-conArea 就是合法摆放位置，
    #     所以DFS，的状态就包括，摆放情况 matrix, 合法摆放位置unchosen, 还剩下皇后数量left
    #     其余的res 和 n 是用来存结果的，可以作为类成员变量存在，而无需放到DFS参数里面
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
    
    # 优化版代码， 
    # 1，每行必有一个Queen， 那么搜索路径可以逐行摆放
    #  2，合法摆放位置，一共四列：（左上-右下， 上-下，左下-右上，左-右），由于是逐行摆放，左右列无需检查，
    #   剩下的三列，可以只需要检查当前位置（x,y)之前的区域，即 a<x,b<y 的区域 (a,b)，其他的区域因为没有摆放Queen，所以没必要检查
    def sovleNQueens_optim(self, n):
        board = [['.']*n for _ in range(n)]
        self.result = []
        self.backTrack(board, 0)
        return self.result

        # DFS 搜索 当前 x 所在row 合法摆放位置
    def backTrack(self, board, x):
        n = len(board)
        # x 递归到 n， 找到结果，终止
        if x >= n:
            res = [''.join(line) for line in board]
            self.result.append(res)
            return
        # 行内寻找合法位置
        for y in range(n):
            if self.isValid(board, x, y):
                board[x][y] = 'Q'
                self.backTrack(board, x+1)
                board[x][y] = '.'
        return

    # 搜索 Queen是否可以摆放到 board 中的（x,y)
    def isValid(self, board, x, y):
        n = len(board)
        # 搜索 x，y 上方是否存在 Queen
        for row in range(x):
            if board[row][y] == "Q":
                return False
        # 搜索 x,y 左上方是否存在 Queen
        for itv in range(1,min(x, y)+1):
            if board[x-itv][y-itv] == 'Q':
                return False
        # 搜索 x,y 右上方是否存在 Queen
        for itv in range(1,x+1):
            if y+itv<n and board[x-itv][y+itv] == "Q":
                return False
        return True

# TODO 双向BFS 

if __name__ == "__main__":
    
    so = Solution()
    # result = so.solveNQueens(4)
    result = so.sovleNQueens_optim(4)
    for r in result:
        print(r)
        print('-'*30)