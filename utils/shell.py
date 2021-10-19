class Solution:
    def shell(self, nums):
        n = len(nums)
        h = 1
        while h < n//3:
           h = 3*h + 1
        # hl = [0,1, 5, 19, 41, 109, 209, 505, 929, 2161, 3905,
        #      8929, 16001, 36289, 64769, 146305, 260609]
        # idx = 0
        # h = hl[idx]
        # while h < n:
        #     idx += 1
        #     h = hl[idx]
        # ht = iter(reversed(hl[ :idx]))
        while h >= 1:
            for i in range(h, n):
                j = i
                while j >= h and nums[j] < nums[j-h]:
                    tmp = nums[j-h]
                    nums[j-h] = nums[j]
                    nums[j] = tmp
                    j = j-h
            #h = next(ht)
            h = h // 3
            #print(h)
        print(nums)
        return nums
if __name__ == "__main__":
    nums = [x for x in range(100000,0,-1)]
    so = Solution()
    res = so.shell(nums)
    
