from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board

        i, j = self.getNextNullPos(0, 0)
        if i != None and j != None:
            unseen = set('123456789') - set(board[i])
            flag = self.getValidSudoku( i, j, unseen)
            return 
        else:
            return 


    def getValidSudoku(self, x, y, unseen):
        if len(unseen) == 0:
            return False
        for e in unseen:
            if not self.isValidElement( x, y , e):
                continue

            self.board[x][y] = e
            if x==8 and y==8:
                return True

            nx, ny = self.getNextNullPos( x, y)
            if nx == None and ny == None:
                return True

            nunseen = set('123456789') - set(self.board[nx])
            flag = self.getValidSudoku( nx, ny ,nunseen)
            if not flag:
                continue
            else:
                return True
                
        self.board[x][y] = '.'
        return False

    def getNextNullPos(self, x, y):
        for i in range(x, 9):
            for j in range(9):
                if self.board[i][j] == '.':
                    return i, j

        return None, None

    def isValidSeq(self, seqs: List[str]) -> bool:
        seqs = [seq for seq in seqs if seq != '.']
        if len(set(seqs)) < len(seqs):
            return False
        return True

    def isValidElement(self, x, y, e):
        # e = board[x][y]
        # board[x][y] = e
        sti = x // 3 * 3
        stj = y // 3 * 3

        seq1 = self.board[x] + [e]
        seq2 = [self.board[k][y] for k in range(9)] + [e]
        seq3 = [self.board[m][n] for m in range(sti, sti+3) for n in range(stj, stj+3)] + [e]

        return self.isValidSeq(seq1) and self.isValidSeq(seq2) and self.isValidSeq(seq3)
    

if __name__ == "__main__":
    so = Solution()
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    res = so.solveSudoku(board)
    
    print(board)