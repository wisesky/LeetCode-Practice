class Solution:
    # def combinationSum(self, candidates: list[int], target: int) -> List[List[int]]:
    def combinationSum(self, candidates, target) :
        dp = [[] for _ in range(target+1)]

        for num in candidates:
            for tgt in range(1, target+1):
                # upidx = tgt
                leftidx = tgt - num 
                
                if leftidx < 0:
                    newLists = []
                elif leftidx == 0 :
                    newLists = [[num]]
                else:
                    newLists = []
                    for newList in dp[leftidx]:
                        nl = newList.copy()
                        nl.append(num)
                        newLists.append(nl)

                dp[tgt] = dp[tgt] + newLists
                
        return dp[-1]

if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7

    candidates = [2,3,5]
    target = 8

    so = Solution()
    print(so.combinationSum(candidates, target))