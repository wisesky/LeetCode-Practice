class Solution:
    # 不用 内置 除法  实现 //
    def divide(self, dividend: int, divisor: int) -> int:

        if (dividend < 0 ) ^ (divisor < 0):
            flag = -1
        else:
            flag = 1 
        
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0        
        while dividend >= divisor:
            # 通过多次减法来实现,每减去一个 divisor , res += add
            temp, add = divisor, 1
            while dividend >= temp:
                # 先减去一个 divisor * add, 同时 res 补上 add个数
                # 随后 divisor * add 加倍, add 同步加倍 
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