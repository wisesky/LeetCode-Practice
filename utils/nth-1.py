class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        r = [1]
        i2, i3, i5 = 0,0,0
        u2, u3, u5 = 2 * r[i2], 3 * r[i3], 5 * r[i5]
        while n > 1:
            
            umin = min(u2, u3, u5)
            r.append(umin)
            if umin == u2 :
                i2 += 1
                u2 = 2 * r[i2]
            if umin == u3:
                i3 += 1
                u3 = 3 * r[i3]
            if umin == u5:
                i5 += 1
                u5 = 2 * r[i5]
            
            n -= 1
        return r[-1]