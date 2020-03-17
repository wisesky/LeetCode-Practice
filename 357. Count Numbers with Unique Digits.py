class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        def res(n, idx):
            if idx > 10:
                return 0
            if n == idx :
                return 1
            if n < idx:
                return 0
            
            return (1 + (10-idx)*res(n,idx+1))
        
        r = res(n,1)*9 + 1
        return r

if __name__ == "__main__":
    so = Solution()
    print(so.countNumbersWithUniqueDigits(3))