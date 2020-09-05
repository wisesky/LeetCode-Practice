from itertools import permutations

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # s1 std lib itertools.permutations
        # perms = permutations(range(1,n+1))
        # perms = list(perms)
        # return ''.join([str(x) for x in perms[k-1]])

        # s2 DFS
        # unused = set(range(1,n+1))
        # res = []
        # self.myPermutations([], unused, res)
        # res.sort()
        # return ''.join([str(x) for x in res[k-1]])

        # s3 BFS
        # unused = set(range(1, n+1))
        # res = [[]]
        # for _ in range(n):
        #     res = self.myPermutations2(res, unused)
        # # res.sort()
        # return ''.join([str(x) for x in res[k-1]])

        # s4 

    # DFS: TLE
    def myPermutations(self,r, unused, res):
        if len(unused) == 0:
            newR = r.copy()
            res.append(newR)
            return
        
        for v in sorted(unused):
            r.append(v)
            self.myPermutations(r , unused - set([v]), res)
            r.pop()
        return

    # BFS: TLE
    def myPermutations2(self, res, unused):
        newRes = [[v] + r for r in res for v in unused if v not in r]
        return newRes

if __name__ == "__main__":
    so = Solution()
    n = 4
    k = 9
    n = 9
    k = 199269
    r = so.getPermutation(n, k)
    print(r)