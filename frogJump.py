class Solution:
    def canCross(self, stones):
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
        if deset[len(stones)-1] == set():
            return False
        return True
if __name__ == "__main__":
    stones = [0, 1, 3, 6, 10, 15, 16, 21]
    so = Solution()
    print(so.canCross(stones))
