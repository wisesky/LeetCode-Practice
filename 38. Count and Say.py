class Solution:
    def countAndSay(self, n: int) -> str:
        i = 1
        es = '1'
        res = []
        while i < n:
            es = self.countStr(es)
            i += 1
        return es


    def countStr(self, es):
        r = ''
        count = 0
        pre = ''
        for i, e in enumerate(es):
            if i == 0:
                pre = e
                count = 1
                continue
            if e == pre:
                count += 1
            else:
                r += str(count) + str(pre)
                count = 1
                pre = e
        r += str(count) + str(pre)
        return r

if __name__ == "__main__":
    so = Solution()
    for i in range(6):
        print(so.countAndSay(i))