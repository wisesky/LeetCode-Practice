from itertools import permutations, product
import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # s1 std lib itertools.permutations AC
        # perms = permutations(range(1,n+1))
        # perms = list(perms)
        # return ''.join([str(x) for x in perms[k-1]])


        # s2 DFS TLE
        # unused = set(range(1,n+1))
        # res = []
        # self.myPermutations([], unused, res)
        # res.sort()
        # return ''.join([str(x) for x in res[k-1]])

        # s3 BFS TLE
        # unused = set(range(1, n+1))
        # res = [[]]
        # for _ in range(n):
        #     res = self.myPermutations2(res, unused)
        # # res.sort()
        # return ''.join([str(x) for x in res[k-1]])

        # s4  permutatiosn src code TLE 
        # pool = range(1, n+1)
        # # perms = self.myPermutationsByProduct(pool)
        # perms = self.permutations(pool)
        # perms = list(perms)
        # return ''.join([str(x) for x in perms[k-1]])

        # s5 数学技巧， 通过判断第k个排列的数学分布规律推断 结果的前缀特征
        # eg： 1开头的排序范围是 1~(n-1)!,  12开头的排序范围是 1~(n-2)!
        #       2开头的排序范围是(n-1)!+1~2*(n-1)! + 1
        return self.mathMethod(n, k)

    # math trick
    def mathMethod(self, n, k):
        nums = list(range(1,n+1))
        perms = ''
        k -= 1
        while n > 0:
            n -= 1
            idx, k = divmod(k, math.factorial(n))
            perms += str(nums[idx])
            nums.remove(nums[idx])

        return perms

    # permutations by product
    def myPermutationsByProduct(self, pool):
        n = len(pool)
        for indices in product(range(n), repeat=n):
            if len(set(indices)) == n:
                yield tuple(pool[i] for i in indices) 

    # std permutatison src
    def permutations(self, iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
        pool = tuple(iterable)
        n = len(pool)
        r = n if r is None else r
        if r > n:
            return
        indices = list(range(n))
        cycles = list(range(n, n-r, -1))
        yield tuple(pool[i] for i in indices[:r])
        while n:
            for i in reversed(range(r)):
                cycles[i] -= 1
                if cycles[i] == 0:
                    indices[i:] = indices[i+1:] + indices[i:i+1]
                    cycles[i] = n - i
                else:
                    j = cycles[i]
                    indices[i], indices[-j] = indices[-j], indices[i]
                    yield tuple(pool[i] for i in indices[:r])
                    break
            else:
                return


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