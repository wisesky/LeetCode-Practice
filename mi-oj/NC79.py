# -*- coding:utf-8 -*-

from collections import deque

class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        # 把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
        
        # s1 TLE
    #     num = 1
    #     count = 1
    #     memo = set([1,2,3,5])

    #     while count != index:
    #         num += 1
    #         res  = self.isUgly(num, memo)
    #         memo.add(res)
    #         if res:
    #             count += 1

    #     if count == index:
    #         return num
    #     else:
    #         return -1


    # def isUgly(self, num, memo):
    #     if num in memo:
    #         return True
        
    #     if num % 5 == 0:
    #         return self.isUgly(num//5, memo)
    #     if num % 3 == 0:
    #         return self.isUgly(num // 3,memo)
    #     if num % 2 == 0:
    #         return self.isUgly(num//2, memo)
    #     return False
        
        # s2 构造丑数
        if index == 0:
            return 0
        res = [1]
        l2 = deque([2])
        l3 = deque([3])
        l5 = deque([5])
        
        v2 = l2.popleft() if len(l2) > 0 else float('inf')
        v3 = l3.popleft() if len(l3) > 0 else float('inf')
        v5 = l5.popleft() if len(l5) > 0 else float('inf')
        l = [l2, l3, l5]
        while len(res) < index:
            val = min(v2, v3, v5)
            res.append(val)

            l2.append(val*2)
            l3.append(val*3)
            l5.append(val*5)

            if v2 == val:
                v2 = l2.popleft()
            if v3 == val:
                v3 = l3.popleft()
            if v5 == val:
                v5 = l5.popleft()

        return res[-1]

if __name__ == '__main__':
    so = Solution()
    index = 7
    print(so.GetUglyNumber_Solution(index))