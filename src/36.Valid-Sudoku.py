import time
from typing import List
import string
from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print('{} take time : {} s'.format( func.__name__,end-start ))
        return r
    return wrapper


class Solution:
    # @timethis
    def isValidSeq(self, seqs: List[str]) -> bool:
        seqs = [seq for seq in seqs if seq != '.']
        if len(set(seqs)) < len(seqs):
            return False
        return True

    def isValidElement(self,  x, y):
        e = board[x][y]
        sti = x // 3 * 3
        stj = y // 3 * 3

        seq1 = board[x]
        seq2 = [board[k][y] for k in range(9)]
        seq3 = [board[m][n] for m in range(sti, sti+3) for n in range(stj, stj+3)]

        return self.isValidSeq(seq1) and self.isValidSeq(seq2) and self.isValidSeq(seq3):
            

    @timethis
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # if board == [
        # [".","8","7","6","5","4","3","2","1"],
        # ["2",".",".",".",".",".",".",".","."],
        # ["3",".",".",".",".",".",".",".","."],
        # ["4",".",".",".",".",".",".",".","."],
        # ["5",".",".",".",".",".",".",".","."],
        # ["6",".",".",".",".",".",".",".","."],
        # ["7",".",".",".",".",".",".",".","."],
        # ["8",".",".",".",".",".",".",".","."],
        # ["9",".",".",".",".",".",".",".","."]
        # ]:
            # return True

        pos = None
        unseen = set()
        for i in range(9):
            # print(board[i])
            if not self.isValidSeq(board[i]):
                return False
            if '.' in board[i]:
                if pos == None :
                    pos = (i, board[i].index('.'))
                    unseen = set('123456789') - set(board[i])
        # print('rows check True')

        for j in range(9):
            seqs = []
            for i in range(9):
                seqs.append(board[i][j])
            if not self.isValidSeq(seqs):
                return False
        # print('columns check True')
        
        for sti in [0, 3, 6]:
            for stj in [0, 3, 6] :
                seqs = []
                for i in range(sti, sti+3):
                    for j in range(stj, stj+3):
                        seqs.append(board[i][j])
                if not self.isValidSeq(seqs):
                    return False
        # print('block check True')

        return True     
        # if pos == None:
        #     return True
        # else: #if pos != None :
        #     for unseenelement in unseen:
        #         board[pos[0]][pos[1]] = unseenelement
        #         r = self.isValidSudoku(board)
        #         board[pos[0]][pos[1]] = '.'
        #         if r == True:
        #             return True
        #         else:
        #             continue
        #     return False
    

if __name__ == "__main__":
    so = Solution()
    # False instance
    board = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
    ]    
    # True instance
    board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
    ]

    # True
    board = [
        [".","8","7","6","5","4","3","2","1"],
        ["2",".",".",".",".",".",".",".","."],
        ["3",".",".",".",".",".",".",".","."],
        ["4",".",".",".",".",".",".",".","."],
        ["5",".",".",".",".",".",".",".","."],
        ["6",".",".",".",".",".",".",".","."],
        ["7",".",".",".",".",".",".",".","."],
        ["8",".",".",".",".",".",".",".","."],
        ["9",".",".",".",".",".",".",".","."]
        ]
    # TLE
    board = [
        [".","8","7","6","5","4","3","2","1"],
        ["2",".",".",".",".",".",".",".","."],
        ["3",".",".",".",".",".",".",".","."],
        ["4",".",".",".",".",".",".",".","."],
        ["5",".",".",".",".",".",".",".","."],
        ["6",".",".",".",".",".",".",".","."],
        ["7",".",".",".",".",".",".",".","."],
        ["8",".",".",".",".",".",".",".","."],
        ["9",".",".",".",".",".",".",".","."]
        ]
    # LTE
    board = [
        [".",".",".",".","4",".","9",".","."],
        [".",".","2","1",".",".","3",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","3"],
        [".",".",".","2",".",".",".",".","."],
        [".",".",".",".",".","7",".",".","."],
        [".",".",".","6","1",".",".",".","."],
        [".",".","9",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","9","."]
        ]
    res = so.isValidSudoku(board)
    print(res)