from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        heigth = len(board)
        if heigth == 0:
            return False
        width = len(board[0])

        for i in range(heigth):
            for j in range(width):
                if board[i][j] == word[0]:
                    marked = {}
                    marked[i,j] = True
                    if self.trySearchChar(board, i, j, word, marked, 1) :
                        return True
        return False

    def trySearchChar(self, board,x, y, word , marked, start):
        heigth = len(board)
        width = len(board[0])
        if start == len(word):
            return True
        
        up = (x-1, y) if x>0 else None
        down = (x+1, y) if x+1<heigth else None
        left = (x, y-1) if y>0 else None
        right = (x,y+1) if y+1<width else None
        char = word[start]
    
        for rd in [up, down, left, right]:
            if rd != None :
                if board[rd[0]][rd[1]] == char and not marked.get(rd, False):
                    marked[rd] = True
                    flag = self.trySearchChar(board, rd[0], rd[1], word,marked, start+1)
                    marked[rd] = False
                    if flag:
                        return True
        return False
        

if __name__ == "__main__":
    so = Solution()
    board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
        ]
    word = 'ABCCED'
    # word = "SEE"
    word = "ABCB"
    board = [['a','a']]
    word = 'aaa'
    flag = so.exist(board, word)
    print(flag)