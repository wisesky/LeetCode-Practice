from typing import List
import heapq
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        length = len(board)
        if length == 0:
            return 
        width = len(board[0])

        q = deque()
        visited = {}
        for i in range(length):
            for j in range(width):
                visited[i, j] = False
                if board[i][j] == 'O':
                    if i in [0, length-1] or j in [0, width-1]:
                        q.append((i,j))
                        visited[i, j] = True

        while len(q) > 0:
            x, y = q.popleft()
            
            up = (x-1,y) if x >= 1 else (None, None)
            down = (x+1, y) if x < length-1 else (None, None)
            left = (x, y-1 )if y-1 >= 0  else (None, None)
            right = (x, y+1) if y < width-1 else (None, None )

            for rd in (up, left, down, right):
                if rd[0] != None:
                    xx, yy = rd
                    if board[xx][yy] == 'O' and not visited[xx, yy]:
                        q.append((xx,yy))
                        visited[xx, yy] = True

        for k in visited:
            if not visited[k]:
                board[k[0]][k[1]] = 'X'
        return

board = [
    ['X' ,'X','X','X'],
    ['X' ,'O','O','X'],
    ['X' ,'X','O','X'],
    ['X' ,'O','X','X']
]

so = Solution()
so.solve(board)

print(board)