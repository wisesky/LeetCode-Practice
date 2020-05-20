class Solution:
    # def removeElement(self, nums: List[int], val: int) -> int:
    def removeElement(self, nums, val) :
        if len(nums) == 0:
            return 0

        # for _ in range(len(nums)):
        #     num = nums.pop()
        #     if num == val:
        #         continue
        #     nums.insert(0, num) 

        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1

        return len(nums)

if __name__ == "__main__":
    so = Solution()
    print(so.removeElement([3,2,2,3], 3))
    print(so.removeElement([0,1,2,2,3,0,4,2], 2))