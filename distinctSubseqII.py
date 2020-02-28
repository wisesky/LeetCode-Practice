class Solution:
    def distinctSubseqII(self, S):
        """
        :type S: str
        :rtype: int
        """
        res = [0] * 26
        for s in S:
            res[ord(s) - ord('a')] = sum(res) + 1
        return sum(res) % (10**9 + 7)
""" import sys
def main(argv):
    sol = Solution()
    print(sol.distinctSubseqII(argv[1]))
if __name__ == "__main__":
    main(sys.argv) """