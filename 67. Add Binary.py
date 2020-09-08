class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l1 = len(a)
        l2 = len(b)

        if l1 >= l2:
            l = l1
            long = a
            short = b
        else:
            l = l2
            long = b
            short = a

        short = short.zfill(l)

        plus = '0'
        res = ''
        for x,y in zip(reversed(long), reversed(short)):
            plus1, r1 = self.addStr(x, y)
            plus2, r2 = self.addStr(r1, plus)
            res = r2 + res
            _, plus = self.addStr(plus1, plus2)

        if plus == '1':
            res = '1' + res

        return res

    def addStr(self, x, y):
        if x == '1' and y == '1':
            return '1', '0'
        elif x == '0' and y == '0':
            return '0','0'
        else:
            return '0','1'

if __name__ == "__main__":
    so = Solution()
    a ,b = '11', '1'
    a = "1010"
    b = "1011"
    res = so.addBinary(a, b)
    print(res)