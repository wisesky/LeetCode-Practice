class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #self.mark = [-1 for _ in nums]
        if len(nums) == 1:
            return nums
        nums = sorted(nums)
        mark = [-1 for _ in nums]
        count = [0 for _ in nums]
        m = -1
        index = -1
        msubs = []
        #self.nums = nums
        for i in range(len(nums)):
            if mark[i] != -1:
                continue
            
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if count[i] < count[j] + 1 :
                        count[i] = count[j] + 1
                        mark[i] = j
                if count[i] > m:
                    m = count[i]
                    index = i
            
        while index != -1 :
            msubs.append(nums[index])
            index = mark[index]

        return msubs

if __name__ == "__main__":
    so = Solution()
    nums = [1,2,3,4]
    print(so.largestDivisibleSubset(nums))