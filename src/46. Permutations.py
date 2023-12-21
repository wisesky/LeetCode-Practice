from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        marked = [False for _ in range(length)]

        result = self.helper(nums, marked)
        return result

    def helper(self, nums, marked):
        length = len(nums)
        if length == 0:
            return [[]]
        
        if length == 1:
            return [nums]

        result = []
        for i,num in enumerate(nums):
            if  not marked[i] :
                marked[i] = True
                r = self.helper(nums, marked)
                marked[i] = False
                res = [[num]+x for x in r]
                result.extend(res)

        return result if len(result) > 0 else  [[]]

    # 回溯算法框架 重构版本
    def permute_traverse(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        length = len(nums)
        self.used = [False for _ in range(length)]
        self.result = []
        # self.traverse([], list(range(length)) )
        self.traverse_2(nums, [])
        return self.result

    # 原始回溯版本，【已选择，未选择】构成遍历状态
    def traverse(self, selectedIdx, reservedIdx):
        if len(reservedIdx) == 0:
            self.result.append([self.nums[idx] for idx in selectedIdx])
            return
        
        for i,chosenIdx in enumerate(reservedIdx):
            if chosenIdx not in selectedIdx:
                self.traverse(selectedIdx+[chosenIdx], reservedIdx[ :i]+reservedIdx[i+1: ])
        return
    
    # 通过 used bool 数组，来过滤出 reservedIdx， 这样就省去reservedIdx的数组以及相关的数组拼接
    def traverse_2(self,nums, selectedIdx):
        if len(selectedIdx) == len(nums):
            self.result.append([self.nums[idx] for idx in selectedIdx])
            return
        
        for i in range(len(nums)):
            # if not self.used[i]:
            #     做选择
            #     self.used[i] = True
            #     self.traverse_2(nums, selectedIdx+[i])
            #     撤销选择
            #     self.used[i] = False
            # 甚至可以通过 selectIdx + [i] 产生新的匿名列表的方式，隐式的完成 做选择 和 撤销选择的 状态改变
            if i not in selectedIdx:
                self.traverse_2(nums, selectedIdx+[i])
        
        return


if __name__ == "__main__":
    nums = [1,2,3]

    so = Solution()
    result = so.permute_traverse(nums)
    print(result)    
    
