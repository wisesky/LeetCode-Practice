from typing import List

def isValidSeq(seqs:List[str]) -> bool:
    seqs = [seq for seq in seqs if seq != '0']
    if len(set(seqs)) < len(seqs):
        return False
    else:
        return True

def isValidElement(matrix, x, y, e):
    stx = x // 3 * 3
    sty = y // 3 * 3

    seq1 = matrix[x] + [e]
    seq2 = [matrix[i][y] for i in range(9)] + [e]
    seq3 = [matrix[i][j] for i in range(stx, stx+3) for j in range(sty, sty+3)] + [e]

    return isValidSeq(seq1) and isValidSeq(seq2) and isValidSeq(seq3)

def getNextNullPos(matrix):
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == '0':
                return i,j
    return None, None

def getValidSudoku(matrix, x, y, unseen):
    if len(unseen) == 0:
        return False

    for e in unseen:
        if not isValidElement(matrix, x, y, e):
            continue

        matrix[x][y] = e
        if x==8 and y==8:
            return True

        nx, ny = getNextNullPos(matrix)
        if nx == None and ny == None:
            return True

        nunseen = set('123456789') - set(matrix[nx])
        flag = getValidSudoku(matrix, nx, ny , nunseen)
        if not flag:
            # matrix[x][y] = '0'
            continue
        else:
            return True

    matrix[x][y] = '0'
    return False

def printMatrix(matrix):
    for i in range(9):
        line = [str(e) for e in matrix[i]]
        text_line = ' '.join(line)
        print(text_line)

while True:
    try:
        matrix = []
        for _ in range(9):
            line = input().split()
            matrix.append(line)
        
        assert len(matrix) == 9 and len(matrix[0]) == 9
        
        x,y = getNextNullPos(matrix)
        if x != None and y != None:
            unseen = set('123456789') - set(matrix[x])
            flag = getValidSudoku(matrix ,x, y, unseen)
            if flag:
                #print
                printMatrix(matrix)
            else:
                print('not valid sukodu')
        else:
            print("can't get 0 postion")

    except:
        break
