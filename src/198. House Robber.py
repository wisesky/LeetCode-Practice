class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[-1]
        r = []
        for i, num in enumerate(nums):
            if i == 0:
                r.append(num)
                continue
            if i-2 < 0:
                res = max(num , r[i-1])
            else:
                res = max(r[i-2] + num, r[i-1])
            r.append(res)
        return max(r)