class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        l1 = len(dungeon)
        l2 = 0 if l1 == 0 else len(dungeon[0])

        r = [float('inf') for _ in range(l2+1)]
        r[-2] = 1

        for i in range(l1, 0, -1):
            #print(r)
            for j in range(l2, 0,-1):
                x = i-1
                y = j-1
                res = min(r[j], r[j-1]) - dungeon[x][y]
                r[j-1] = max(res, 1)
            #print(r)
        return r[0]
if __name__ == "__main__":
    dun = [
        [-2,-3,3],
        [-5,-10,1],
        [10,30, -5]
    ] 
    #dun = [[-200]]
    #dun = [[1, -3, 3], [0, -2, 0], [-3, -3, -3]]
    so = Solution()
    res = so.calculateMinimumHP(dun)
    print(res)
