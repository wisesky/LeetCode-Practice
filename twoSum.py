class Solution:
    def twoSum(self, nums=[2,7,11,15], target = 9) :
        
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        d = {}
        for i in range(len(nums)):
            res = target - nums[i]
            if d.get(res) != None:
                return [d.get(res), i]
            d[nums[i]] = i
        return False

if __name__ == "__main__":
    #argv = sys.argv
    #nums = argv[0]
    #target = argv[1]
    #main()
    nums = [2, 7,11, 15]
    target = 9
    so = Solution()
    res = so.twoSum(nums, target)
    print(res)
