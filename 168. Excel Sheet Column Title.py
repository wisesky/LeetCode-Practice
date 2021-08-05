class Solution:
    # 无位值进制
    # 特殊规则的26进制：满26用26（z）表示， 满27才进一，且直接跳过0，数字范围： 1-26
    # eg ：Y(25) -> Z(26) -> A(1)A(1)
    # 常规26进制， 满26进1， 数字范围 0-25
    def convertToTitle(self, n: int) -> str:
        r = []
        while n > 0:
            c = n % 26
            if c == 0:
                c = 26
                n -= 1
            r.append(chr(ord('A') + c - 1))
            n = n // 26
        return ''.join(reversed(r))

so = Solution()
print(so.convertToTitle(701))
        