class Solution:
    def canCross(self, stones):
        # 此题的关键是： 
        # deset 记录并更新可以到达当前石头的之前jump 距离
        # ntoidx   石头位置：石头序号
        deset = {i:set() for i in range(len(stones))}
        ntoidx = {n:i for i,n in enumerate(stones)}
        deset[1].add(1)
        for i in range(1, len(stones)):
            #if deset[i] == set():
             #   return False
            for j in deset[i]:
                nextJump = stones[i+1: ]
                de = stones[i] + j
                de1 = de+1
                de0 = de-1
                if de in nextJump:
                    #idx = ntoidx[de]
                    deset[ntoidx[de]].add(j)
                if de1 in nextJump:
                    deset[ntoidx[de1]].add(j+1)
                if de0 in nextJump:
                    deset[ntoidx[de0]].add(j-1)
        if len( deset[len(stones)-1] )== 0:
            return False
        return True
if __name__ == "__main__":
    stones = [0, 1, 3, 6, 10, 15, 16, 21]
    so = Solution()
    print(so.canCross(stones))
