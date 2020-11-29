#
# return the min number
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def minNumberdisappered(self , arr ):
        # write code here  
        
        # idx = float('inf')
        for i, num in enumerate(arr):
            if num == 1:
                break
        else:
            return 1
        
        st = 2
        pos = i+1
        while pos in range(len(arr)) and arr[pos] == st:
            st += 1
            pos += 1
        
        return st

l = [-1,2,3,4,]
l = [1,2,3,5]
so = Solution()
res = so.minNumberdisappered(l)
print(res)
