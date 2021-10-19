class Solution:
    #count = 0
    def permutation(self, freeznum, changenum,reverse=False):
        if not reverse:
            if self.count > self.k:
                return
        else:
            if self.end - self.count + 1 < self.k:
                return 
        if len(changenum) == 1:
            tmp = freeznum + list(changenum)
            self.count += 1
            if not reverse:
                if self.count == self.k:
                    self.res.append(tmp)
            else:
                if self.end - self.count + 1 == self.k:
                   self.res.append(tmp)
            return 
        for x in sorted(changenum, reverse=reverse):
            freeznum.append(x)
            self.permutation(freeznum, changenum.difference([x]), reverse=reverse)
            freeznum.pop(-1)
        return
    def getPermutation(self, n, k):
        e = [i for i in range(1,n+1)]
        self.count = 0
        self.k = k
        end = 1
        for x in e:
            end = end*x
        self.end = end
        self.res = []
        self.permutation([], set(e), reverse= k > end // 2)
        self.res = [int(''.join(str(l) for l in r)) for r in self.res]
        print('res : ' , self.res[: ])
        return str(self.res[0])
if __name__ == "__main__":
    s = Solution()
    print(s.getPermutation(9,62716))
    #print(s.getPermutation(2, 2))
