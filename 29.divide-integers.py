class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        if (dividend < 0 ) ^ (divisor < 0):
            flag = -1
        else:
            flag = 1 
        
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0        
        while dividend >= divisor:
            temp, add = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += add
                temp <<= 1
                add <<= 1

        res = flag * res
        return min(max(res, -2**31), 2**31 - 1)
        
if __name__ == "__main__":
    so = Solution()
    print(so.divide(10, 3))
    print(so.divide(-7, 3))