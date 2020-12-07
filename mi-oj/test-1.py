#coding=utf-8
import sys 
#str = input()
#print(str)
#print('Hello,World!')

def findPath(map):
    length1 = len(map)
    if length1 == 0:
        return 0
    length2 = len(map[0])

    dp = [[0]*length2 for _ in range(length1)]

    for i in range(length1):
        for j in range(length2):
            if i==0 and j==0 :
                if map[i][j] == 0:
                    return 0
                else:
                    dp[0][0] = 1
                continue

            val = map[i][j]
            if val == 1:
                up = dp[i-1][j] if i>=1 else 0
                left = dp[i][j-1] if j>= 1 else 0
                dp[i][j] = up + left

    return dp[-1][-1]

map = [
    [0,1,0],
    [0,1,1],
    [0,0,1],
    [1,0,1]
]

r = findPath(map)
print(r)