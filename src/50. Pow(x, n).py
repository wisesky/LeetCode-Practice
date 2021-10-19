import math
class Solution:
    def dpow(self, x, n, d) :
        if n in d:
            return d[n]

        sqt = n // 2
        rest = n - 2*sqt
        r_sqt = self.dpow(x, sqt, d)
        r_rest = self.dpow(x, rest, d)
        res = r_sqt ** 2 * r_rest
        d[n] = res
        return res

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        abs_n = abs(n)
        flag = n // abs_n

        d = {1:x,0:1}
        r = x
        # way 1 :AC
        i = 1
        acc = math.ceil(math.log2(abs_n))
        
        for _ in range(acc):
            r *= r
            i *= 2
            d[i] = r
        
        while i != abs_n:
            if i > abs_n:
                r = r/x
                i = i - 1
            elif i < abs_n:
                r = r*x
                i = i + 1
        
        # way 2 Numercal result out of range
        # r = self.dpow(x, abs_n, d)    

        # way 3 
        # i = 1
        # while i < abs_n:
        #     j = 1
        #     r_j = x
        #     while i+j < abs_n:
        #         r_j = x * r_j
        #         j += 1
        #     r = r*r_j
        #     i = i + j
        
        if flag == -1:
            r = 1/r
        return r

if __name__ == "__main__":
    so = Solution()
    x = 2
    n = 10
    x = 0.00001
    n = 2147483647
    x = 2
    n = -2147483648
    r = so.myPow(x, n)
    print(r)
